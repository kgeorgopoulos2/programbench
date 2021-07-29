import pandas
import csv
import numpy as np

def singleQubitErrorRates(data):
    '''Returns as a dictionary the single qubit error rates, as they appear on ibmq_16_melbourne. NOTE: the 
    values deviate every time the machine gets callibrated.'''
    qubits = data.Qubit.tolist()
    del qubits[0]
    rates = data.SQError.tolist()
    del rates[0]
    sqRates = dict(zip(qubits, rates))
    
    return sqRates

def twoQubitErrorRates(data):
    '''Returns as a dictionary the two qubit error rates, as they appear on ibmq_16_melbourne. NOTE: the values 
    deviate every time the machine gets callibrated.'''
    tqer = data.TQError.tolist()
    del tqer[0]

    qpairs = []
    qvals = []
    for i in range(0, len(tqer)):
        tqer[i] = tqer[i].replace("cx", "Q")

        s = tqer[i].split(",")
        for j in range(0, len(s)):
            t = s[j].split(":")
            qpairs.append(t[0].replace(" ", ""))
            qvals.append(float(t[1].replace(" ", "")))

    tqRates = dict(zip(qpairs, qvals))
    
    return tqRates

def measureErrorRates(data):
    '''Returns as a dictionary the measurement error rates, as they appear on ibmq_16_melbourne. NOTE: the values
    deviate every time the machine gets callibrated'''
    qubits = data.Qubit.tolist()
    del qubits[0]
    rates = data.ReadoutError.tolist()
    del rates[0]
    measRates = dict(zip(qubits, rates))
    
    return measRates

def getDecoherenceTimes(data):
    '''Returns the thermal relaxation time T1 and the qubit dephasing time T2, as given by IBMQ.'''
    t1er = data.T1.tolist()
    del t1er[0]
    t2er = data.T2.tolist()
    del t2er[0]

    for i in range(0, len(t1er)):
        t1er[i] = float(t1er[i] + "e3")
        t2er[i] = float(t2er[i] + "e3")

    T1s = np.array(t1er)
    T2s = np.array(t2er)
    
    # Check for error in IBMQ's measurements (i.e it must always be T2 <= 2T1)
    c = 0
    for i in range(0,len(T1s)):
        if (T2s[i] > 2*T1s[i]):
            c = 1
            print("ERROR: incompatible decay rates - Qubit Q", i, ", T2 =", T2s[i], "and T1 =", T1s[i])
    if (c == 0):
        print(r'Checking decoherence times: all ok')

    return T1s,T2s