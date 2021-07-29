q = QuantumRegister(5, 'q')
c = ClassicalRegister(4, 'c')
circ = QuantumCircuit(q, c)
circ.rz(pi/2, q[0])
circ.sx(q[0])
circ.rz(pi/2, q[0])
circ.rz(3*pi/2, q[1])
circ.sx(q[1])
circ.rz(pi/2, q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(pi/2, q[2])
circ.sx(q[2])
circ.rz(pi/2, q[2])
circ.rz(3*pi/2, q[3])
circ.sx(q[3])
circ.rz(pi/2, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[3],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.rz(3*pi/2, q[0])
circ.sx(q[0])
circ.rz(pi/2, q[0])
circ.rz(15*pi/8, q[1])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[3],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(-3*pi/8, q[1])
circ.sx(q[1])
circ.rz(pi/2, q[1])
circ.rz(pi/2, q[2])
circ.sx(q[2])
circ.rz(3*pi/2, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.x(q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(3*pi/2, q[3])
circ.sx(q[3])
circ.rz(13*pi/8, q[3])
circ.cx(q[3],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[3],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[3],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[3],q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(5*pi/8, q[0])
circ.sx(q[0])
circ.rz(3*pi/2, q[0])
circ.rz(pi/2, q[1])
circ.sx(q[1])
circ.rz(3*pi/2, q[1])
circ.rz(pi/2, q[2])
circ.sx(q[2])
circ.rz(3*pi/2, q[2])
circ.rz(pi/2, q[3])
circ.sx(q[3])
circ.rz(3*pi/2, q[3])
circ.barrier()
circ.x(q[1])
circ.x(q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[3],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(-3*pi/8, q[0])
circ.sx(q[0])
circ.rz(pi/2, q[0])
circ.rz(pi/2, q[1])
circ.sx(q[1])
circ.rz(3*pi/2, q[1])
circ.rz(3*pi/2, q[2])
circ.sx(q[2])
circ.rz(3*pi/2, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.x(q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(3*pi/2, q[3])
circ.sx(q[3])
circ.rz(pi/2, q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[3],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[0])
circ.rz(pi/8, q[0])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[3],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[2],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.rz(pi/2, q[0])
circ.sx(q[0])
circ.rz(3*pi/2, q[0])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.rz(pi/2, q[1])
circ.sx(q[1])
circ.rz(3*pi/2, q[1])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/2, q[2])
circ.sx(q[2])
circ.rz(3*pi/2, q[2])
circ.rz(5*pi/8, q[3])
circ.sx(q[3])
circ.rz(3*pi/2, q[3])
circ.barrier()
circ.x(q[1])
circ.x(q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(15*pi/8, q[1])
circ.rz(pi/8, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.rz(pi/8, q[1])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[3])
circ.rz(pi/8, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(pi/8, q[2])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.rz(pi/2, q[1])
circ.sx(q[1])
circ.rz(pi/2, q[1])
circ.rz(15*pi/8, q[2])
circ.rz(pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/8, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.rz(3*pi/2, q[0])
circ.sx(q[0])
circ.rz(3*pi/2, q[0])
circ.x(q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(pi/8, q[1])
circ.rz(pi/8, q[2])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/2, q[2])
circ.sx(q[2])
circ.rz(3*pi/2, q[2])
circ.rz(-3*pi/8, q[3])
circ.sx(q[3])
circ.rz(pi/2, q[3])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[1],q[0])
circ.rz(15*pi/8, q[0])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[0],q[1])
circ.rz(15*pi/8, q[1])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(pi/8, q[1])
circ.cx(q[1],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[1],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.x(q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[2],q[1])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(15*pi/8, q[3])
circ.cx(q[3],q[2])
circ.rz(pi/8, q[2])
circ.cx(q[3],q[2])
circ.rz(15*pi/8, q[2])
circ.cx(q[2],q[3])
circ.cx(q[3],q[2])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(pi/8, q[2])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.x(q[1])
circ.cx(q[0],q[1])
circ.cx(q[1],q[0])
circ.cx(q[0],q[1])
circ.rz(pi/2, q[0])
circ.sx(q[0])
circ.rz(pi/2, q[0])
circ.rz(15*pi/8, q[2])
circ.rz(pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/8, q[3])
circ.cx(q[2],q[3])
circ.cx(q[1],q[2])
circ.rz(pi/2, q[1])
circ.sx(q[1])
circ.rz(3*pi/2, q[1])
circ.rz(pi/8, q[2])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(15*pi/8, q[3])
circ.cx(q[2],q[3])
circ.rz(pi/2, q[2])
circ.sx(q[2])
circ.rz(3*pi/2, q[2])
circ.rz(5*pi/8, q[3])
circ.sx(q[3])
circ.rz(3*pi/2, q[3])
circ.barrier()
circ.measure(q[1], c[0])
circ.measure(q[0], c[1])
circ.measure(q[2], c[2])
circ.measure(q[3], c[3])