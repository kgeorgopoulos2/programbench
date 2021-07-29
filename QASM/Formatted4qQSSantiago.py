q = QuantumRegister(5, 'q')
c = ClassicalRegister(4, 'c')
circ = QuantumCircuit(q, c)
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
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
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
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
circ.rz(pi/2, q[4])
line = 'circ.rz(pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.sx(q[4])
line = 'circ.sx(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(pi/2, q[4])
line = 'circ.rz(pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
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
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3*pi/2, q[1])
line = 'circ.rz(3*pi/2, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(13*pi/8, q[1])
line = 'circ.rz(13*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3*pi/2, q[2])
line = 'circ.rz(3*pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(-3*pi/8, q[3])
line = 'circ.rz(-3*pi/8, q[3])'
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
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.x(q[3])
line = 'circ.x(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(3*pi/2, q[4])
line = 'circ.rz(3*pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.sx(q[4])
line = 'circ.sx(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(pi/2, q[4])
line = 'circ.rz(pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
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
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3*pi/2, q[2])
line = 'circ.rz(3*pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
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
circ.rz(pi/2, q[4])
line = 'circ.rz(pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.sx(q[4])
line = 'circ.sx(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(3*pi/2, q[4])
line = 'circ.rz(3*pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.barrier()
circ.x(q[2])
line = 'circ.x(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.x(q[3])
line = 'circ.x(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
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
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-3*pi/8, q[1])
line = 'circ.rz(-3*pi/8, q[1])'
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
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3*pi/2, q[2])
line = 'circ.rz(3*pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.x(q[1])
line = 'circ.x(q[1])'
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
circ.rz(13*pi/8, q[3])
line = 'circ.rz(13*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.x(q[4])
line = 'circ.x(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[4])
line = 'circ.rz(15*pi/8, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.x(q[3])
line = 'circ.x(q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
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
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3*pi/2, q[2])
line = 'circ.rz(3*pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/2, q[4])
line = 'circ.rz(pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.sx(q[4])
line = 'circ.sx(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(3*pi/2, q[4])
line = 'circ.rz(3*pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.barrier()
circ.x(q[2])
line = 'circ.x(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.x(q[4])
line = 'circ.x(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi/8, q[1])
line = 'circ.rz(pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
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
circ.rz(pi/2, q[3])
line = 'circ.rz(pi/2, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(15*pi/8, q[1])
line = 'circ.rz(15*pi/8, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-3*pi/8, q[1])
line = 'circ.rz(-3*pi/8, q[1])'
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
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3*pi/2, q[2])
line = 'circ.rz(3*pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.x(q[1])
line = 'circ.x(q[1])'
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
circ.rz(13*pi/8, q[3])
line = 'circ.rz(13*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.x(q[4])
line = 'circ.x(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[4])
line = 'circ.rz(15*pi/8, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[4])
line = 'circ.rz(pi/8, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[3],q[2])
line = 'circ.cx(q[3],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[2])
line = 'circ.rz(15*pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[4],q[3])
line = 'circ.cx(q[4],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[3],q[4])
line = 'circ.cx(q[3],q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/8, q[3])
line = 'circ.rz(pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
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
circ.rz(pi/8, q[2])
line = 'circ.rz(pi/8, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(15*pi/8, q[3])
line = 'circ.rz(15*pi/8, q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.cx(q[2],q[3])
line = 'circ.cx(q[2],q[3])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[3])	elif (dep == ['Y']):		circ.y(q[3])	else:		circ.z(q[3])
circ.rz(pi/2, q[2])
line = 'circ.rz(pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3*pi/2, q[2])
line = 'circ.rz(3*pi/2, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(5*pi/8, q[3])
line = 'circ.rz(5*pi/8, q[3])'
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
circ.rz(pi/2, q[4])
line = 'circ.rz(pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.sx(q[4])
line = 'circ.sx(q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.rz(3*pi/2, q[4])
line = 'circ.rz(3*pi/2, q[4])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[4])	elif (dep == ['Y']):		circ.y(q[4])	else:		circ.z(q[4])
circ.barrier()
line = 'circ.measure(q[1], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[1])
circ.measure(q[1], c[0])
line = 'circ.measure(q[4], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[4])
circ.measure(q[4], c[1])
line = 'circ.measure(q[2], c[2])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[2])
circ.measure(q[2], c[2])
line = 'circ.measure(q[3], c[3])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[3])
circ.measure(q[3], c[3])