OPENQASM 2.0;
include "qelib1.inc";

// Zero-Noise Extrapolation — noise scale factor 3
// Same logical circuit as scale1, but with identity
// replaced by cx-cx pairs to increase noise

qreg q[2];
creg c[1];

// Prepare |+⟩
h q[0];

// Noise amplification: 2 extra CNOT pairs (identity logically)
// Each cx-cx pair adds gate noise without changing the state
cx q[0], q[1];
cx q[0], q[1];    // pair 1: identity

cx q[0], q[1];
cx q[0], q[1];    // pair 2: identity

// Measure in X basis
h q[0];
measure q[0] -> c[0];
