q = QuantumRegister(7, 'q')
c = ClassicalRegister(2, 'c')
circ = QuantumCircuit(q, c)
circ.rz(pi/2, q[0])
line = 'circ.rz(pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3082593, q[0])
line = 'circ.rz(3.3082593, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi, q[1])
line = 'circ.rz(pi, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(4.7397129, q[0])
line = 'circ.rz(4.7397129, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.3355832, q[0])
line = 'circ.rz(3.3355832, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3.6486287, q[0])
line = 'circ.rz(3.6486287, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(2.0778324, q[0])
line = 'circ.rz(2.0778324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(6.1165186, q[1])
line = 'circ.rz(6.1165186, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3*pi/2, q[0])
line = 'circ.rz(3*pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3*pi/2, q[0])
line = 'circ.rz(3*pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[1])
line = 'circ.measure(q[0], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[0], c[0])
line = 'circ.measure(q[1], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[1], c[1])