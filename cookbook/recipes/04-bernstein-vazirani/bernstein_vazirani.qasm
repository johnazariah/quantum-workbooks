OPENQASM 2.0;
include "qelib1.inc";

// Bernstein-Vazirani algorithm
// Hidden string: s = 101 (decimal 5)

qreg q[4];   // q[0..2] = input register; q[3] = ancilla
creg c[3];   // measure input register

// Step 1: Prepare ancilla in |−⟩
x q[3];
h q[3];

// Step 2: Superposition on input register
h q[0];
h q[1];
h q[2];

// Step 3: Oracle for f(x) = s·x mod 2, with s = 101
// CNOT from each qubit i where s_i = 1
cx q[0], q[3];   // s_0 = 1
// skip q[1]       // s_1 = 0
cx q[2], q[3];   // s_2 = 1

// Step 4: Hadamard on input register
h q[0];
h q[1];
h q[2];

// Step 5: Measure
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
