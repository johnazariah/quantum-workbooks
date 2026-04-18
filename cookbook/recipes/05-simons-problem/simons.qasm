OPENQASM 2.0;
include "qelib1.inc";

// Simon's algorithm for a 2-bit hidden period
// Hidden string: s = 11
// Oracle implements f such that f(x) = f(x XOR s)
// f(00) = f(11) = 00, f(01) = f(10) = 01

qreg q[4];   // q[0..1] = input register; q[2..3] = output register
creg c[2];   // measure input register only

// Step 1: Superposition on input register
h q[0];
h q[1];

// Step 2: Oracle for f with period s = 11
// Copy input to output: f(x) = x (before period structure)
cx q[0], q[2];
cx q[1], q[3];
// Add period structure: if q[0]=1, XOR output with s=11
cx q[0], q[2];
cx q[0], q[3];

// Step 3: Hadamard on input register
h q[0];
h q[1];

// Step 4: Measure input register
measure q[0] -> c[0];
measure q[1] -> c[1];
