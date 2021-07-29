# Importing libraries
import numpy as np
import scipy
from scipy.linalg import expm, sinm, cosm
import itertools, functools
from math import sqrt, log
from cmath import sqrt as csqrt
from collections import OrderedDict

# Importing Qiskit
from qiskit.quantum_info.operators import Operator
from qiskit import Aer, BasicAer, IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.extensions import HamiltonianGate
from qiskit.aqua.utils import tensorproduct

def decompose_pauli(H, N):
    '''Implements the Pauli decomposition of an arbitrary Hamiltonian. Returns the decomposition in the form
    of a list of matrices.'''
    # Define the Pauli matrices
    sx = np.array([[0, 1],  [1, 0]], dtype=np.complex128) # Pauli X matrix
    sy = np.array([[0, -1j],[1j, 0]], dtype=np.complex128) # Pauli Y matrix
    sz = np.array([[1, 0],  [0, -1]], dtype=np.complex128) # Pauli Z matrix
    iden = np.array([[1, 0],  [ 0, 1]], dtype=np.complex128) # Identity matrix
    S = [iden, sx, sy, sz]
    dec = []
    alf = []
    ref = []
    it = 0
    
    # Do the decomposition
    for ms in itertools.product(S, repeat=int(np.log2(N))):
        M = functools.reduce(lambda x, y: np.kron(x,y), ms) # Calculating the tensor product
        alpha = (1/N) * (np.dot(M, H).trace()) # Calculating alpha
        
        if (alpha != (0.+0.j)):
            dec.append(alpha*M)
            alf.append(alpha)
            ref.append(it)
        
        it = it + 1
        
    return dec,alf,ref

def evaluate_decomposition(result, H, N):
    '''Evaluates the result of the decomposition.'''
    correct = True
    for i in range(0, N):
        for j in range(0, N):
            if (sum(result)[i][j] != H[i][j]):
                print("Approximation error: " + str(sum(result)[i][j]) + " instead of " + str(H[i][j]) +
                      "in element (" + str(i) + "," + str(j) + ").")
                correct = False

    if (correct == True):
        print("Successful evaluation")
        
    return None

def matprint(mat, fmt="g"):
    "Neatly prints a matrix."
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")
        
    return None
                
def hamiltonian(N):
    '''Returns the operator containing the Hamiltonian, H, for the CTQW evolution.'''
    # ATTENTION: H=A*1/d, where A is the adjacency matrix mapping the circle
    miHt = np.array([
        [0.+0.j]*N
    ]*N)

    miHt[0][N-1] = 1/2
    miHt[N-1][0] = 1/2
    for i in range(0, N):
        for j in range(0, N):
            if (j == i+1) or (j == i-1):
                miHt[i][j] = 1/2

    return miHt

def hamiltonian_mit(N, t):
    '''Returns the Hamiltonian operator before exponentiation.'''
    # ATTENTION: this representation containes the experssion -iHt, i.e the power of the expression e^{-iHt}, and H=A*1/d => (0.-1.j) = -i
    miHt = np.array([
        [0.+0.j]*N
    ]*N)

    miHt[0][N-1] = (0.-1.j)*t/2
    miHt[N-1][0] = (0.-1.j)*t/2
    for i in range(0, N):
        for j in range(0, N):
            if (j == i+1) or (j == i-1):
                miHt[i][j] = (0.-1.j)*t/2

    return miHt

def hamiltonian_exponential(N, t):
    '''Returns the operator resulting from the Hamiltonian exponentiation.'''
    # ATTENTION: this representation containes the experssion -iHt, i.e the power of the expression e^{-iHt}, and H=A*1/d => (0.-1.j) = -i
    miHt = np.array([
        [0.+0.j]*N
    ]*N)

    miHt[0][N-1] = (0.-1.j)*t/2
    miHt[N-1][0] = (0.-1.j)*t/2
    for i in range(0, N):
        for j in range(0, N):
            if (j == i+1) or (j == i-1):
                miHt[i][j] = (0.-1.j)*t/2

    # Perform the exponent e^{-iHt}
    exp_miHt = scipy.linalg.expm(miHt)

    return exp_miHt

def get_labels(N):
    '''Returns all the tensor products of Pauli operators in the sum (including those with alpha = 0).
    ATTENTION: it iterates in the same order as the `decompose_pauli()` method.'''
    labels = ['I', 'X', 'Y', 'Z']
    ret = []
    
    for pair in itertools.product(labels, repeat=int(np.log2(N))):
        ret.append(pair)
    
    return ret

def get_sum_terms(l, alpha, ref):
    '''Prints out the terms of the Pauli decomposition.'''
    terms = ['']*len(ref)
    
    for i in range(0, len(ref)):
        terms[i] = (str(alpha[i]) + '*' + str(l[ref[i]]))
        
    return terms

def getQState(qwalk, n):
    '''Method to get the quantum state before the measurement.'''
    sv_simulator = Aer.get_backend('statevector_simulator')

    # Execute and get counts
    result = execute(qwalk, sv_simulator).result()
    statevector = result.get_statevector(qwalk)

    # statevector

    b = []
    for k in range(0,len(statevector)):
        b.append(k)

    i = iter(statevector)
    j = iter(b)
    dct = dict(zip(j, i))

    # Create the dictionary without all the    
    qstate = {}
    for i in range(0,len(dct)):
        qstate[format(i, '0'+str(n)+'b')] = dct[i]
                                    
    return qstate

def getNonZeros(dct):
    '''Method that returns the positions of the state space that have non-zero amplitudes in
    the form of a dictionary.'''
    non_zeros = dict()

    for key in dct.keys():
        if (dct[key] != (0+0j)):
            non_zeros[key] = dct[key]
            
    return non_zeros

def get_statevector_probabilities(dct, n):
    '''Methods that calculates the probabilities of each position of the state space from
    the amplitudes of the quantum state. Returns a dictionary that contains the states with
    removed the ancilla and coin qubits.'''
    dct = getNonZeros(dct)
    probs = dict()
    
    probs = {k[-n:]:0 for k,v in dct.items()}
    for k,v in dct.items():
        probs[k[-n:]]+=np.abs(v)**2
    
    dec = [0]*len(probs.keys())
    probs_dec = dict()
    
    for key in probs.keys():
        probs_dec[int(key, 2)] = probs[key]
    
    return probs_dec

def get_ctqw_pos_prob(n, t, meas):
    '''Method that returns the positions of the particle for a single number of coin flips,
    as well as the probabilities for the walker to be at each of the states.'''
    
    qwalk = ctqw(n, t, meas) # Return the CTQW circuit
    qstate = getQState(qwalk, n) # Return the statevector (i.e quantum state before measurement)
    dct = get_statevector_probabilities(qstate, n)
    
    pos = list(dct.keys())
    prob = list(dct.values())
    
    return pos,prob

def unitaryHam(N, t):
    '''Returns the operator resulting from the Hamiltonian exponentiation.'''
    # Define the Hamiltonian
    H = np.array([
        [0.+0.j]*N
    ]*N)

    H[0][N-1] = 1/2
    H[N-1][0] = 1/2
    for i in range(0, N):
        for j in range(0, N):
            if (j == i+1) or (j == i-1):
                H[i][j] = 1/2

    H = Operator(H)
    
    expHam = HamiltonianGate(H, t, label='CTQW') # This format includes time, t

    return expHam

def ctqw(n, t, meas):
    '''Creates the continues time quantum walk circuit on an N-cycle'''
    N = 2**n
    U_c = unitaryHam(N, t)
    
    q = QuantumRegister(n, 'q')
    c = ClassicalRegister(n, 'c')
    circ = QuantumCircuit(q, c)

    circ.append(U_c, [q[i] for i in range(0, n)])
    
    if (meas == True):
        circ.measure(q,c)
    
    return circ

def check_commute(products, N):
    '''Checking if the terms of the decomposition commute'''
    test = np.zeros((N, N))
    commute = True
    for i in range(0, len(products)):
        for j in range(0, len(products)):
            if (((np.dot(products[i], products[j]) - np.dot(products[j], products[i]))==test).all()==False):
                commute = False
    
    if (commute == True):
        print("All terms commute.")
    else:
        print("Commutation violated - use Lie product formula.")

    return None

def check_hermitian(products):
    '''Checking if the terms of the decomposition are Hermitian'''
    hermitian = True
    for i in range(0, len(products)):
        if ((products[i].conjugate().transpose()==products[i]).all() == False):
            print("Term t" + str(i+1) + " is not Hermitian.")
            hermitian = False
            
    if (hermitian == True):
        print("All tensored exponents are Hermitian.")
    
    return None

def lie_product_formula(products, r, t):
    '''Evaluates the precision of the Pauli decomposition using the Lie product formula.'''
    mul = scipy.linalg.expm((-1.j)*products[0]*t/r)
    for i in range(1, len(products)):
        mul = mul@(scipy.linalg.expm((-1.j)*products[i]*t/r))
    
    # Calculate the Hamiltonian with precision r
    ham = mul
    for i in range(0, r):
        ham = mul@ham
    
    return ham

def matrix_distance(A, B, choice):
    '''Calculates the distance between two matrices.'''
    d = 0
    if (choice == "d1"):
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                d = d + np.absolute(A[i][j] - B[i][j])
    elif (choice == "d2"):
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                d = d + (A[i][j] - B[i][j])**2
        d = csqrt(d)
    elif (choice == "dinf"):
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                d = max(d, np.absolute(A[i][j] - B[i][j]))
    elif (choice == "L2"):
        d = np.linalg.norm(A-B)
    else:
        print("Not valid distance.")

    return d

def get_product_terms(terms):
    '''Returns a list containing the exponents along with the alpha scalars; the exponents does not include -h or t.'''
    sx = np.array([[0, 1],  [1, 0]], dtype=np.complex128) # Pauli X matrix
    sy = np.array([[0, -1j],[1j, 0]], dtype=np.complex128) # Pauli Y matrix
    sz = np.array([[1, 0],  [0, -1]], dtype=np.complex128) # Pauli Z matrix
    iden = np.array([[1, 0],  [ 0, 1]], dtype=np.complex128) # Identity matrix
    
    p = [None]*len(terms)
    for i in range(0, len(terms)):
        s1 = terms[i].split('*')
        s2 = s1[1].split(', ')
        ten = [None]*len(s2)
        for j in range(0, len(s2)):
            if ('I' in s2[j]):
                ten[j] = iden
            elif ('X' in s2[j]):
                ten[j] = sx
            elif ('Y' in s2[j]):
                ten[j] = sy
            else:
                ten[j] = sz
        p[i] = np.complex128(s1[0])*tensorproduct(*ten)
        
    return p

def decomp_circuit(gates, r, n, lie):
    '''Creates the circuit that implements the Hamiltonian decomposition.'''
    q = QuantumRegister(n, 'q')
    c = ClassicalRegister(n, 'c')
    circ = QuantumCircuit(q, c)
    
    if (lie == True):
        for j in range(0, int(r)):
            for k in range(0, len(gates)):
                circ.append(gates[k], [q[i] for i in range(0, n)])

        circ.measure(q, c)
    else:
        for k in range(0, len(gates)):
            circ.append(gates[k], [q[i] for i in range(0, n)])
        
        circ.measure(q, c)
    
    return circ

def hellingerDistance(p, q):
    '''Calculate the Hellinger distance between two probability distributions, P and Q. P and Q aregiven as simple 
    arrays containing the probabilities p[i] and q[i]. IMPORTANT: the probability arrays have to be ordered in the 
    same way.'''
    sum = 0
    for i in range (0, len(p)):
        sum = sum + (np.sqrt(p[i]) - np.sqrt(q[i]))**2
        
    h = (1/np.sqrt(2))*np.sqrt(sum)
        
    return h

def get_dist_probabilities(dct,N):
    '''Creates list of probabilities from the given line of data.'''
    p = list(dct.values())
    for i in range(0,len(p)):
        p[i] = p[i]/N
    
    return p

def add_missing_counts(dct, N):
    '''Adds missing counts on a dictionary with probability 0.'''
    k = list(dct.keys())
    v = list(dct.values())
    
    for i in range(0, N):
        if (str(bin(i)[2:].zfill(int(log(N, 2)))) not in k):
            k.append(bin(i)[2:].zfill(int(log(N, 2))))
            v.append(0)
    
    dct = dict(zip(k, v))
    dct = dict(OrderedDict(sorted(dct.items())))
    
    return dct

def get_d_with_var_epsilon(H, dType, varEpsilon):
    '''Returns a list containing the distances of type dType for every epsilon in the list varEpsilon.'''
    d = [None]*len(varEpsilon)
    
    for i in range(0, len(varEpsilon)):
        r = ((scipy.linalg.norm(H)*t)**2)/varEpsilon[i] # Number of iterations of the decomposition
        mul = lie_product_formula(products, int(r)) # Calculate mul matrix
        d[i] = matrix_distance(H, mul, dType) # Calculate the distance for this i
    
    return d

def get_helD_with_var_epsilon(simIterations, n, t, varEpsilon):
    '''Returns a list containing the Hellinger distances between the ideal counts and
    the counts computed for each varEpsilon.'''
    hd = [None]*(len(varEpsilon)-4)
    
    # Run the ideal simulation
    ctq_walk = ctqw(n, t, meas=True)

    simulate = execute(ctq_walk, backend=simulator, shots=simIterations).result()
    ideal_counts = simulate.get_counts()
    ideal_counts = dict(OrderedDict(sorted(ideal_counts.items())))
    ideal_counts = add_missing_counts(ideal_counts, N)
    
    for i in range(0, len(varEpsilon)-4):
        print(r"Simulating for epsilon =", varEpsilon[i])
        r = ((scipy.linalg.norm(H)*t)**2)/varEpsilon[i]
        gates = [HamiltonianGate(products[i], t/r) for i in range(0, len(products))]
        
        # Execute the evolution
        dcirc = decomp_circuit(gates, r, n, True)
        simulate = execute(dcirc, backend=simulator, shots=simIterations).result()
        counts = simulate.get_counts()
        counts = dict(OrderedDict(sorted(counts.items())))
        counts = add_missing_counts(counts, N)
        
        hd[i] = hellingerDistance(get_dist_probabilities(ideal_counts, simIterations), get_dist_probabilities(counts, simIterations))
    
    return hd