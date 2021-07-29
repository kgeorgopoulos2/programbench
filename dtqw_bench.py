# Import libraries
import time, ast, re
import numpy as np
from numpy import pi as pi
from collections import OrderedDict
import matplotlib.pyplot as plt
import importlib
import sys

# Import Qiskit
from qiskit import Aer, IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram

# Importing Python Files
import qwalk
import QASMParser
import unm

# Loading account and defining variables
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q-research', group='newcastle-1', project='main')
simulator = Aer.get_backend("qasm_simulator")
qc_iterations = 5000 # Iterations per experiment run on the quantum computer
trials = 20 # Number of trials on the quantum computer, each one is run for qc_iterations iterations
sim_iterations = 100000 # Iterations on the simulator (i.e., qc_iterations*trials)

# Functions
def getExData(exFilename, prob, iterations):
    '''Returns the data as list of dictionaries. prob - True if we want the data to be returned as probability
    distributions instead of counts. NOTE: careful with the name of the datafiles.'''
    path = "/Users/b6035076/Qiskit/qiskit-tutorials-master/PhD Research/Program Benchmarking Quantum Machines/Data/"
    with open(path + exFilename) as f:
        content = f.readlines()
    experimentData = [ast.literal_eval(x.strip('\n')) for x in content]
    f.close()

    # Format the lists with probabilities instead of counts of positions
    if (prob==True):
        for i in range(0,len(experimentData)):
            dct = ast.literal_eval(experimentData[i])
            keys = list(dct.keys())
            values = list(dct.values())
            for j in range(0,len(values)):
                values[j] = values[j]/iterations
            dct = dict(zip(keys, values))
            experimentData[i] = (str(dct))
        
    return experimentData

def getAvgData(data):
    '''Returns the average distribution of all the data collected from the trials on the quantum computer.'''
    avg_dct = dict()
    
    for key in data[0].keys():
        sm = 0
        for i in range(0,len(data)):
            sm = sm + data[i][key]
            
        avg_dct[key] = sm/len(data)
    
    return avg_dct

def getSumData(data):
    '''Returns the cummulative distribution as the sum of the counts for all trials.'''
    sum_dct = dict()
    
    for key in data[0].keys():
        sm = 0
        for i in range (0, len(data)):
            sm = sm + data[i][key]
            
        sum_dct[key] = sm
    
    return sum_dct

def qwNoiseExecute(iterations, thermal, backend, T1s, T2s, graph, gates):
    '''This method executes the circuit. This is necessary, since the circuit has to be generated each time for the new gates to appear'''
    counts = [{}]*iterations
    
    if (thermal == False):
        for i in range(0,iterations):
            sys.stdout.write('\r'+"Simulation count: "+str(i+1))
            circ = qwQASM()
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), shots=1).result()
            counts[i] = simulate.get_counts()
    else:
        noise_thermal = unm.thermalRelaxationChannel(backend, T1s, T2s, graph, gates)
        for i in range(0,iterations):
            sys.stdout.write('\r'+"Simulation count: "+str(i+1))
            circ = qwQASM()
            simulate = execute(circ, backend = Aer.get_backend("qasm_simulator"), basis_gates=noise_thermal.basis_gates, 
                               noise_model=noise_thermal, shots=1).result()
            counts[i] = simulate.get_counts()
    
    return counts

def qwQASM():
    '''Runs the formatted python file and returns the circuit.'''
    sys.path.insert(1, 'QASM')
    import Formatted2qQW
    
    circ = Formatted2qQW.run()
        
    return circ

def noiseFreeqwQASM():
    '''Runs the formatted, noise-free python file and returns the circuit.'''
    sys.path.insert(1, 'QASM')
    import NoiseFreeFormatted2qQW
    
    circ = NoiseFreeFormatted2qQW.run()
    
    return circ

########## Benchmarking the IBMQx5 Bogota machine ##########
# Creating architectural awareness specific for the quantum circuit run
gates = [2, 3, 4] # The qubits that participate in the circuit
graph = [[2,3], [3,2], [3,4], [4,3]] # The pairs of qubits that participate in the circuit

# Printing the machine data
datafile = "2qQWDataBogota.txt" # IMPORTANT: select the correct machine
exData = getExData(datafile, False, qc_iterations)
print("Quantum computer data:", exData)
avgExData = getAvgData(exData)
print("\nAverage counts on quantum computer trials for", qc_iterations, "iterations:", avgExData)
sumExData = getSumData(exData)
print("\nSum counts on quantum computer trials for", trials, "trials and", qc_iterations, "iterations each trial:", sumExData, "\n")

# Preparing the error rates and noise data
path_data = "Data/ibmq_bogota_calibrations_2qQW.csv"
data = unm.machineData(path_data)
thermal = True
sqRates = unm.getSingleQubitErrorRates(data) # Dictionary containing the single qubit error rates
tqRates = unm.getTwoQubitErrorRates(data) # Dictionary containing the two qubit error rates
measRates = unm.getMeasureErrorRates(data) # Dictionary containing the measurement error rates per qubit
T1s,T2s = unm.getDecoherenceTimes(data)

# Getting information about the quantum circuit
circ = noiseFreeqwQASM()
circ_size = circ.size()
circ_depth = circ.depth()
circ_width = circ.width()

print("Number of gates in the QASM circuit (including measurements):", circ_size) # number of gates in the circuit
# The length of the longest path from the input (or from a preparation) to the output (or a measurement gate), moving forward in time along qubit wires.
print("Depth of the QASM circuit:", circ_depth)
print("Number of qubits in the QASM circuit:", circ_width, "\n") # contains the number of qubits + the number of clbits

# Specify the device
device = provider.get_backend('ibmq_bogota')
print("Simulations of the '" + str(device) + "' machine quantum evolution.")

# UNM simulations
start_time = time.time()
counts_comb = qwNoiseExecute(sim_iterations, thermal, device, T1s, T2s, graph, gates)
end_time = time.time()
print("\nTime elapsed:", end_time - start_time, "seconds.")
counts_comb = unm.getCounts(counts_comb, sim_iterations)
counts_comb = dict(OrderedDict(sorted(counts_comb.items())))
print("\nCounts on noisy quantum simulator:", counts_comb)