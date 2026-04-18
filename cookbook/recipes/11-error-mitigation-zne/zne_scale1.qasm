OPENQASM 2.0;
include "qelib1.inc";

// Zero-Noise Extrapolation — noise scale factor 1 (base circuit)
// Circuit: prepare |+⟩ state and measure in X basis
// Ideal ⟨X⟩ = 1.0; noisy value will be less

qreg q[1];
creg c[1];

// Prepare |+⟩
h q[0];

// Identity (noise scale λ = 1)
// No extra gates

// Measure in X basis
h q[0];
measure q[0] -> c[0];
