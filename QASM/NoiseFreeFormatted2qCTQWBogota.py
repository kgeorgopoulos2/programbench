q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')
circ = QuantumCircuit(q, c)
circ.rz(3*pi/2, q[0])
circ.sx(q[0])
circ.rz(3*pi/2, q[1])
circ.sx(q[1])
circ.rz(pi, q[1])
circ.cx(q[0],q[1])
circ.rz(3.6486287, q[0])
circ.sx(q[0])
circ.sx(q[0])
circ.rz(2.0778324, q[0])
circ.rz(6.1415927, q[1])
circ.sx(q[1])
circ.cx(q[0],q[1])
circ.rz(1.4292037, q[0])
circ.sx(q[0])
circ.rz(pi/2, q[0])
circ.rz(pi/2, q[1])
circ.measure(q[0], c[0])
circ.measure(q[1], c[1])