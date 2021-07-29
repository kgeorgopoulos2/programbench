# Import the necessary libraries
import numpy as np
from math import pi as pi

# importing QISKit
from qiskit import Aer, IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

def qft_dagger(circ, q, t):
    """n-qubit QFTdagger the first n qubits in circ"""
    # Don't forget the Swaps!
    for qubit in range(t//2):
        circ.swap(q[qubit], q[t-qubit-1])
    for j in range(t):
        for m in range(j):
            circ.cu1(-np.pi/float(2**(j-m)), q[m], q[j])
        circ.h(q[j])
        
    return circ

def qpe(angle, n):
    '''Creates the QPE circuit that estimates the specified angle in an n-size system. Returnes: circ - the QPE circuit.'''
    q = QuantumRegister(n, 'q')
    c = ClassicalRegister(n-1, 'c')
    circ = QuantumCircuit(q, c)
    
    # Initialize in |psi> = 1
    circ.x(q[n-1])
    for i in range(0,n-1):
        circ.h(q[i])
        
    # Apply QFT
    repetitions = 1
    for counting_qubit in range(0,n-1):
        for i in range(repetitions):
            circ.cu1(angle, q[counting_qubit], q[n-1]); # This is C-U
        repetitions *= 2
    circ.barrier()
    
    # Apply inverse QFT
    circ = qft_dagger(circ, q, n-1)
    circ.barrier()
    
    # Measure
    for i in range(0,n-1):
        circ.measure(q[i], c[i])
    
    return circ