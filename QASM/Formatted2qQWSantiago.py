q = QuantumRegister(5, 'q')
c = ClassicalRegister(2, 'c')
circ = QuantumCircuit(q, c)
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[3])
line = 'circ.rz(7*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[3])
line = 'circ.rz(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[3])
line = 'circ.rz(7*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[4])
line = 'circ.rz(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[2])
line = 'circ.rz(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.x(q[2])
line = 'circ.x(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[3])
line = 'circ.rz(7*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[4])
line = 'circ.rz(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[4])
line = 'circ.rz(7*pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[3])
line = 'circ.rz(pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[3])
line = 'circ.rz(7*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[4])
line = 'circ.rz(pi/4, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(pi/4, q[2])
line = 'circ.rz(pi/4, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.rz(7*pi/4, q[3])
line = 'circ.rz(7*pi/4, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):
circ.x(q[2])
line = 'circ.x(q[2])'
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
circ.barrier()
line = 'circ.measure(q[3], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[3], c[0])
line = 'circ.measure(q[4], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):
circ.measure(q[4], c[1])