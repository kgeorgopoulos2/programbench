q = QuantumRegister(7, 'q')
c = ClassicalRegister(4, 'c')
circ = QuantumCircuit(q, c)
circ.rz(3*pi/2, q[0])
line = 'circ.rz(3*pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[0])
line = 'circ.rz(pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[3])
line = 'circ.rz(3*pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[5])
line = 'circ.rz(pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.sx(q[5])
line = 'circ.sx(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(pi/2, q[5])
line = 'circ.rz(pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(-3*pi/8, q[0])
line = 'circ.rz(-3*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[0])
line = 'circ.rz(pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[3])
line = 'circ.rz(3*pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(3*pi/2, q[3])
line = 'circ.rz(3*pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.x(q[3])
line = 'circ.x(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.x(q[5])
line = 'circ.x(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/2, q[0])
line = 'circ.rz(pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3*pi/2, q[0])
line = 'circ.rz(3*pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(5*pi/8, q[1])
line = 'circ.rz(5*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(3*pi/2, q[3])
line = 'circ.rz(3*pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[5])
line = 'circ.rz(pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.sx(q[5])
line = 'circ.sx(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(3*pi/2, q[5])
line = 'circ.rz(3*pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.barrier()
circ.x(q[3])
line = 'circ.x(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.x(q[5])
line = 'circ.x(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(-3*pi/8, q[0])
line = 'circ.rz(-3*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[0])
line = 'circ.rz(pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.x(q[0])
line = 'circ.x(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3*pi/2, q[3])
line = 'circ.rz(3*pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(13*pi/8, q[3])
line = 'circ.rz(13*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.x(q[5])
line = 'circ.x(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[5])
line = 'circ.rz(15*pi/8, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.x(q[3])
line = 'circ.x(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(5*pi/8, q[0])
line = 'circ.rz(5*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3*pi/2, q[0])
line = 'circ.rz(3*pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/2, q[5])
line = 'circ.rz(pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.sx(q[5])
line = 'circ.sx(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(3*pi/2, q[5])
line = 'circ.rz(3*pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.barrier()
circ.x(q[1])
line = 'circ.x(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.x(q[5])
line = 'circ.x(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.x(q[1])
line = 'circ.x(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(-3*pi/8, q[0])
line = 'circ.rz(-3*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[0])
line = 'circ.rz(pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.x(q[0])
line = 'circ.x(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3*pi/2, q[5])
line = 'circ.rz(3*pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.sx(q[5])
line = 'circ.sx(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(3*pi/2, q[5])
line = 'circ.rz(3*pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[5])
line = 'circ.cx(q[3],q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[5],q[3])
line = 'circ.cx(q[5],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[3])
line = 'circ.cx(q[1],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/8, q[0])
line = 'circ.rz(pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[3],q[1])
line = 'circ.cx(q[3],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(15*pi/8, q[0])
line = 'circ.rz(15*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(5*pi/8, q[0])
line = 'circ.rz(5*pi/8, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3*pi/2, q[0])
line = 'circ.rz(3*pi/2, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi/2, q[1])
line = 'circ.rz(pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.sx(q[3])
line = 'circ.sx(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(3*pi/2, q[3])
line = 'circ.rz(3*pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[5])
line = 'circ.rz(pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.sx(q[5])
line = 'circ.sx(q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.rz(3*pi/2, q[5])
line = 'circ.rz(3*pi/2, q[5])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[5])	elif (dep == ['Y']):		circ.y(q[5])	else:		circ.z(q[5])
circ.barrier()
line = 'circ.measure(q[3], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[3])
circ.measure(q[3], c[0])
line = 'circ.measure(q[5], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[5])
circ.measure(q[5], c[1])
line = 'circ.measure(q[1], c[2])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[1])
circ.measure(q[1], c[2])
line = 'circ.measure(q[0], c[3])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[0])
circ.measure(q[0], c[3])