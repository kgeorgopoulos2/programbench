q = QuantumRegister(7, 'q')
c = ClassicalRegister(2, 'c')
circ = QuantumCircuit(q, c)
circ.rz(pi/2, q[5])
line = 'circ.rz(pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[5])
line = 'circ.sx(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[5])
line = 'circ.rz(pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[5])
line = 'circ.rz(7*pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[6])
line = 'circ.rz(pi/2, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[6])
line = 'circ.sx(q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[6])
line = 'circ.rz(pi/2, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[5])
line = 'circ.rz(pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[4])
line = 'circ.rz(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[5])
line = 'circ.rz(7*pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[4])
line = 'circ.rz(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[5])
line = 'circ.rz(7*pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[6])
line = 'circ.rz(pi/4, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.x(q[6])
line = 'circ.x(q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[4])
line = 'circ.rz(7*pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[5])
line = 'circ.rz(pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[4])
line = 'circ.rz(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[5])
line = 'circ.rz(7*pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[5])
line = 'circ.cx(q[4],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[5],q[4])
line = 'circ.cx(q[5],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(3*pi/4, q[4])
line = 'circ.rz(3*pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[4])
line = 'circ.sx(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[4])
line = 'circ.rz(pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[5])
line = 'circ.rz(7*pi/4, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[6])
line = 'circ.rz(pi/4, q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[6],q[5])
line = 'circ.cx(q[6],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.x(q[6])
line = 'circ.x(q[6])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.barrier()
line = 'circ.measure(q[5], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[5], c[0])
line = 'circ.measure(q[4], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[4], c[1])