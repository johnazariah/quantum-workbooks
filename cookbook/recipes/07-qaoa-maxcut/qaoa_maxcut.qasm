OPENQASM 2.0;
include "qelib1.inc";

// QAOA for MaxCut on a triangle graph.
// Edges: (0,1), (0,2), (1,2)
// Depth: p = 1
//
// Circuit convention:
//   edge block = cx; rz(2 * gamma); cx
//   mixer      = rx(2 * beta)
//
// Fixed angles for this triangle instance:
//   gamma = 1.264491043069892  -> rz(2.528982)
//   beta  = 0.3063052837250049 -> rx(0.612611)

qreg q[3];
creg c[3];

// Step 1: Equal superposition over all 8 cuts.
h q[0];
h q[1];
h q[2];

// Step 2: One ZZ phase block per graph edge.
// Edge (0,1)
cx q[0], q[1];
rz(2.528982) q[1];
cx q[0], q[1];

// Edge (0,2)
cx q[0], q[2];
rz(2.528982) q[2];
cx q[0], q[2];

// Edge (1,2)
cx q[1], q[2];
rz(2.528982) q[2];
cx q[1], q[2];

// Step 3: Mixer.
rx(0.612611) q[0];
rx(0.612611) q[1];
rx(0.612611) q[2];

// Step 4: Measure one candidate cut.
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
