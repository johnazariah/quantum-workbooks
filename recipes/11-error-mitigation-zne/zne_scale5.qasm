OPENQASM 2.0;
include "qelib1.inc";

// Zero-Noise Extrapolation — noise scale factor 5
// Same logical circuit with more noise-amplifying gates

qreg q[2];
creg c[1];

// Prepare |+⟩
h q[0];

// Noise amplification: 4 extra CNOT pairs
cx q[0], q[1];
cx q[0], q[1];    // pair 1

cx q[0], q[1];
cx q[0], q[1];    // pair 2

cx q[0], q[1];
cx q[0], q[1];    // pair 3

cx q[0], q[1];
cx q[0], q[1];    // pair 4

// Measure in X basis
h q[0];
measure q[0] -> c[0];
