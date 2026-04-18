OPENQASM 2.0;
include "qelib1.inc";

// 3-qubit Quantum Fourier Transform
// Input: |5⟩ = |101⟩

qreg q[3];
creg c[3];

// Prepare input state |101⟩ = |5⟩
x q[0];
x q[2];

// QFT on 3 qubits
// Qubit 0 (most significant)
h q[0];
cp(1.5708) q[1], q[0];   // controlled-S (π/2)
cp(0.7854) q[2], q[0];   // controlled-T (π/4)

// Qubit 1
h q[1];
cp(1.5708) q[2], q[1];   // controlled-S (π/2)

// Qubit 2
h q[2];

// Swap q[0] and q[2] to fix bit ordering
swap q[0], q[2];

// Measure
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
