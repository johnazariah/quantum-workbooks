OPENQASM 2.0;
include "qelib1.inc";

// QAOA for MaxCut on a triangle graph (3 nodes, 3 edges)
// Edges: (0,1), (1,2), (0,2)
// p = 1 layer
// Optimal parameters: gamma ≈ π/4, beta ≈ π/8

qreg q[3];
creg c[3];

// Step 1: Initial superposition
h q[0];
h q[1];
h q[2];

// Step 2: Problem unitary — exp(-i * gamma * C) with gamma = pi/4
// Edge (0,1): exp(-i * gamma * Z0 Z1)
cx q[0], q[1];
rz(0.7854) q[1];    // rz(pi/4) = rz(gamma)
cx q[0], q[1];

// Edge (1,2): exp(-i * gamma * Z1 Z2)
cx q[1], q[2];
rz(0.7854) q[2];
cx q[1], q[2];

// Edge (0,2): exp(-i * gamma * Z0 Z2)
cx q[0], q[2];
rz(0.7854) q[2];
cx q[0], q[2];

// Step 3: Mixer unitary — exp(-i * beta * X) with beta = pi/8
rx(0.3927) q[0];    // rx(pi/8) = rx(beta)  [note: rx(θ) = exp(-iθX/2), so rx(2*beta)]
rx(0.3927) q[1];
rx(0.3927) q[2];

// Step 4: Measure
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
