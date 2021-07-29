q = QuantumRegister(5, 'q')
c = ClassicalRegister(2, 'c')
circ = QuantumCircuit(q, c)
circ.rz(pi/2, q[2])
circ.sx(q[2])
circ.rz(pi/2, q[2])
circ.rz(pi/2, q[3])
circ.sx(q[3])
circ.rz(pi/2, q[3])
circ.cx(q[4],q[3])
circ.rz(7*pi/4, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/4, q[3])
circ.cx(q[4],q[3])
circ.rz(7*pi/4, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.rz(pi/4, q[2])
circ.x(q[2])
circ.rz(7*pi/4, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/4, q[4])
circ.cx(q[3],q[4])
circ.rz(7*pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.rz(pi/4, q[3])
circ.cx(q[4],q[3])
circ.rz(7*pi/4, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/4, q[4])
circ.cx(q[3],q[4])
circ.cx(q[4],q[3])
circ.cx(q[3],q[4])
circ.cx(q[2],q[3])
circ.rz(pi/4, q[2])
circ.rz(7*pi/4, q[3])
circ.cx(q[2],q[3])
circ.x(q[2])
circ.rz(3*pi/4, q[4])
circ.sx(q[4])
circ.rz(pi/2, q[4])
circ.barrier()
circ.measure(q[3], c[0])
circ.measure(q[4], c[1])