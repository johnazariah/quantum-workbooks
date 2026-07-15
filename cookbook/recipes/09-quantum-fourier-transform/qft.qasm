OPENQASM 2.0;
include "qelib1.inc";

// 3-qubit Quantum Fourier Transform
// Input: |5> = |101> in displayed order q[0] q[1] q[2]

qreg q[3];
creg c[3];

// Prepare input state |101> = |5>
x q[0];
x q[2];

// QFT on 3 qubits
h q[0];
cu1(1.5708) q[1], q[0];   // controlled phase pi/2
cu1(0.7854) q[2], q[0];   // controlled phase pi/4

h q[1];
cu1(1.5708) q[2], q[1];   // controlled phase pi/2

h q[2];

// Restore displayed bit order
swap q[0], q[2];

// Measure
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
