q = QuantumRegister(5, 'q')
c = ClassicalRegister(3, 'c')
circ = QuantumCircuit(q, c)
circ.rz(1.1933502, q[0])
line = 'circ.rz(1.1933502, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(0.53112886, q[0])
line = 'circ.rz(0.53112886, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
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
circ.rz(4.8101638, q[2])
line = 'circ.rz(4.8101638, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.4555106, q[2])
line = 'circ.rz(4.4555106, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(2.4173381, q[2])
line = 'circ.rz(2.4173381, q[2])'
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
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-0.87145697, q[1])
line = 'circ.rz(-0.87145697, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.8069458, q[1])
line = 'circ.rz(4.8069458, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-1.8288536, q[1])
line = 'circ.rz(-1.8288536, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.6405925, q[2])
line = 'circ.rz(1.6405925, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.8288536, q[1])
line = 'circ.rz(1.8288536, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.8069458, q[1])
line = 'circ.rz(4.8069458, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(0.87145697, q[1])
line = 'circ.rz(0.87145697, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-1.61512, q[0])
line = 'circ.rz(-1.61512, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.9339053, q[0])
line = 'circ.rz(4.9339053, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(2.7481368, q[0])
line = 'circ.rz(2.7481368, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(-2.4173381, q[1])
line = 'circ.rz(-2.4173381, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.4555106, q[1])
line = 'circ.rz(4.4555106, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.7176941, q[1])
line = 'circ.rz(2.7176941, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(-1.1870848, q[0])
line = 'circ.rz(-1.1870848, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.6691491, q[0])
line = 'circ.rz(4.6691491, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.934116, q[0])
line = 'circ.rz(4.934116, q[0])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.3490693, q[1])
line = 'circ.rz(1.3490693, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.6691491, q[1])
line = 'circ.rz(4.6691491, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.1870848, q[1])
line = 'circ.rz(1.1870848, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-1.5713867, q[0])
line = 'circ.rz(-1.5713867, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.6750979, q[0])
line = 'circ.rz(4.6750979, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3.1732507, q[0])
line = 'circ.rz(3.1732507, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3.5350485, q[1])
line = 'circ.rz(3.5350485, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.9339053, q[1])
line = 'circ.rz(4.9339053, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.5742172, q[1])
line = 'circ.rz(3.5742172, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(-1.6024324, q[0])
line = 'circ.rz(-1.6024324, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.711799, q[0])
line = 'circ.rz(4.711799, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.6750979, q[0])
line = 'circ.rz(4.6750979, q[0])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.6080874, q[1])
line = 'circ.rz(1.6080874, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.711799, q[1])
line = 'circ.rz(4.711799, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.6024324, q[1])
line = 'circ.rz(1.6024324, q[1])'
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
circ.rz(-3.7313119, q[0])
line = 'circ.rz(-3.7313119, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(5.8566486, q[0])
line = 'circ.rz(5.8566486, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(2.9568654, q[0])
line = 'circ.rz(2.9568654, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(-1.2377277, q[1])
line = 'circ.rz(-1.2377277, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.1339458, q[1])
line = 'circ.rz(4.1339458, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.1131891, q[1])
line = 'circ.rz(2.1131891, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-2.1131891, q[1])
line = 'circ.rz(-2.1131891, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.1339458, q[1])
line = 'circ.rz(4.1339458, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(0.43181258, q[1])
line = 'circ.rz(0.43181258, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(1.9746981, q[0])
line = 'circ.rz(1.9746981, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.7821986, q[0])
line = 'circ.rz(4.7821986, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(1.2329445, q[0])
line = 'circ.rz(1.2329445, q[0])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.9086481, q[1])
line = 'circ.rz(1.9086481, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.6425794, q[1])
line = 'circ.rz(4.6425794, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.9746981, q[1])
line = 'circ.rz(1.9746981, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-2.7344615, q[1])
line = 'circ.rz(-2.7344615, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(5.0347069, q[1])
line = 'circ.rz(5.0347069, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.0541354, q[1])
line = 'circ.rz(3.0541354, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-1.5632295, q[2])
line = 'circ.rz(-1.5632295, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.2668013, q[2])
line = 'circ.rz(4.2668013, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3.1081959, q[2])
line = 'circ.rz(3.1081959, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
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
circ.rz(1.6009318, q[2])
line = 'circ.rz(1.6009318, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.705561, q[2])
line = 'circ.rz(4.705561, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(2.0163952, q[2])
line = 'circ.rz(2.0163952, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
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
circ.rz(1.1251975, q[2])
line = 'circ.rz(1.1251975, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.719217, q[2])
line = 'circ.rz(4.719217, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(1.6009318, q[2])
line = 'circ.rz(1.6009318, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(-1.5705925, q[1])
line = 'circ.rz(-1.5705925, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.6864966, q[1])
line = 'circ.rz(4.6864966, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.1258524, q[1])
line = 'circ.rz(3.1258524, q[1])'
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
circ.rz(-1.3138149, q[1])
line = 'circ.rz(-1.3138149, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.45977, q[1])
line = 'circ.rz(3.45977, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.7881478, q[1])
line = 'circ.rz(2.7881478, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.1081959, q[2])
line = 'circ.rz(3.1081959, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(5.1579767, q[2])
line = 'circ.rz(5.1579767, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3.19922, q[2])
line = 'circ.rz(3.19922, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-2.7881478, q[1])
line = 'circ.rz(-2.7881478, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.45977, q[1])
line = 'circ.rz(3.45977, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.3230188, q[1])
line = 'circ.rz(1.3230188, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(1.390043, q[0])
line = 'circ.rz(1.390043, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.6849709, q[0])
line = 'circ.rz(4.6849709, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(1.2705056, q[0])
line = 'circ.rz(1.2705056, q[0])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.8710871, q[1])
line = 'circ.rz(1.8710871, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.739807, q[1])
line = 'circ.rz(4.739807, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.390043, q[1])
line = 'circ.rz(1.390043, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
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
circ.rz(-1.6188349, q[1])
line = 'circ.rz(-1.6188349, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.6090025, q[1])
line = 'circ.rz(4.6090025, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.0109999, q[1])
line = 'circ.rz(4.0109999, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-1.4191612, q[0])
line = 'circ.rz(-1.4191612, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(5.8143749, q[0])
line = 'circ.rz(5.8143749, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3.3875914, q[0])
line = 'circ.rz(3.3875914, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(2.2721854, q[1])
line = 'circ.rz(2.2721854, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.6090025, q[1])
line = 'circ.rz(4.6090025, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.8582914, q[1])
line = 'circ.rz(2.8582914, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(2.8955939, q[0])
line = 'circ.rz(2.8955939, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(5.8143749, q[0])
line = 'circ.rz(5.8143749, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(1.6891418, q[0])
line = 'circ.rz(1.6891418, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(1.475088, q[2])
line = 'circ.rz(1.475088, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.5989008, q[2])
line = 'circ.rz(4.5989008, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(1.3786143, q[2])
line = 'circ.rz(1.3786143, q[2])'
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
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.1400427, q[1])
line = 'circ.rz(2.1400427, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.7881885, q[1])
line = 'circ.rz(4.7881885, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.3130243, q[1])
line = 'circ.rz(1.3130243, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-4.3162449, q[1])
line = 'circ.rz(-4.3162449, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.5056337, q[1])
line = 'circ.rz(4.5056337, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.524978, q[1])
line = 'circ.rz(2.524978, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-1.5573908, q[0])
line = 'circ.rz(-1.5573908, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.4616765, q[0])
line = 'circ.rz(4.4616765, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3.0353122, q[0])
line = 'circ.rz(3.0353122, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(2.5494257, q[1])
line = 'circ.rz(2.5494257, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.454287, q[1])
line = 'circ.rz(4.454287, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(1.9935408, q[1])
line = 'circ.rz(1.9935408, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-2.6715254, q[2])
line = 'circ.rz(-2.6715254, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3.3456395, q[2])
line = 'circ.rz(3.3456395, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.4331665, q[2])
line = 'circ.rz(4.4331665, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(-4.4331665, q[2])
line = 'circ.rz(-4.4331665, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3.3456395, q[2])
line = 'circ.rz(3.3456395, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(1.2970787, q[2])
line = 'circ.rz(1.2970787, q[2])'
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
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3.2478731, q[0])
line = 'circ.rz(3.2478731, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.4616765, q[0])
line = 'circ.rz(4.4616765, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(0.37929351, q[0])
line = 'circ.rz(0.37929351, q[0])'
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
circ.rz(-1.7357912, q[1])
line = 'circ.rz(-1.7357912, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.1948948, q[1])
line = 'circ.rz(4.1948948, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.747173, q[1])
line = 'circ.rz(3.747173, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.5360123, q[1])
line = 'circ.rz(2.5360123, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.1948948, q[1])
line = 'circ.rz(4.1948948, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(0.95039308, q[1])
line = 'circ.rz(0.95039308, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(-1.7127748, q[2])
line = 'circ.rz(-1.7127748, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.2255787, q[2])
line = 'circ.rz(4.2255787, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(3.6993655, q[2])
line = 'circ.rz(3.6993655, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(-1.5479599, q[2])
line = 'circ.rz(-1.5479599, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.7121282, q[2])
line = 'circ.rz(4.7121282, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.7352254, q[2])
line = 'circ.rz(4.7352254, q[2])'
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
circ.cx(q[0],q[1])
line = 'circ.cx(q[0],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.7150066, q[0])
line = 'circ.rz(4.7150066, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi, q[0])
line = 'circ.rz(pi, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(2.4369311, q[1])
line = 'circ.rz(2.4369311, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(4.2912131, q[1])
line = 'circ.rz(4.2912131, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(2.4369311, q[1])
line = 'circ.rz(2.4369311, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
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
circ.rz(3.0766018, q[0])
line = 'circ.rz(3.0766018, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(4.6475349, q[0])
line = 'circ.rz(4.6475349, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(3.9290998, q[0])
line = 'circ.rz(3.9290998, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(pi, q[2])
line = 'circ.rz(pi, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(2.7740525, q[2])
line = 'circ.rz(2.7740525, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.cx(q[1],q[2])
line = 'circ.cx(q[1],q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.rz(4.799821, q[2])
line = 'circ.rz(4.799821, q[2])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[2])	elif (dep == ['Y']):		circ.y(q[2])	else:		circ.z(q[2])
circ.sx(q[2])
line = 'circ.sx(q[2])'
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
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(5.6773796, q[0])
line = 'circ.rz(5.6773796, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
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
circ.cx(q[1],q[0])
line = 'circ.cx(q[1],q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.rz(5.483103, q[0])
line = 'circ.rz(5.483103, q[0])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[0])	elif (dep == ['Y']):		circ.y(q[0])	else:		circ.z(q[0])
circ.sx(q[0])
line = 'circ.sx(q[0])'
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
circ.cx(q[2],q[1])
line = 'circ.cx(q[2],q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(pi, q[1])
line = 'circ.rz(pi, q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.sx(q[1])
line = 'circ.sx(q[1])'
op = noisyGate(line, sqRates, tqRates)
if (op == ['X']):	dep = list(np.random.choice(['X', 'Z', 'Y'], p=[0.5,0.1,0.4]))	if (dep == ['X']):		circ.x(q[1])	elif (dep == ['Y']):		circ.y(q[1])	else:		circ.z(q[1])
circ.rz(3.808532, q[1])
line = 'circ.rz(3.808532, q[1])'
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
circ.barrier()
line = 'circ.measure(q[1], c[0])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[1])
circ.measure(q[1], c[0])
line = 'circ.measure(q[2], c[1])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[2])
circ.measure(q[2], c[1])
line = 'circ.measure(q[0], c[2])'
op = noisyMeasure(line, measRates)
if (op == ['X']):	circ.x(q[0])
circ.measure(q[0], c[2])