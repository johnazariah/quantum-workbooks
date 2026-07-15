OPENQASM 2.0;
include "qelib1.inc";

// Quantum Phase Estimation for the T gate
// T|1> = exp(2*pi*i/8)|1>, so phase phi = 1/8.
// Three counting qubits give resolution 1/8.

qreg q[4];   // q[0..2] = counting register, displayed as q[0] q[1] q[2]
creg c[3];   // measure counting register

// Step 1: prepare eigenstate |1>
x q[3];

// Step 2: put the counting register into superposition
h q[0];
h q[1];
h q[2];

// Step 3: controlled powers of U = T
cu1(0.7854) q[2], q[3];   // controlled T
cu1(1.5708) q[1], q[3];   // controlled T^2 = controlled S
cu1(3.1416) q[0], q[3];   // controlled T^4 = controlled Z

// Step 4: inverse QFT on the counting register
swap q[0], q[2];
h q[2];
cu1(-1.5708) q[2], q[1];
h q[1];
cu1(-0.7854) q[2], q[0];
cu1(-1.5708) q[1], q[0];
h q[0];

// Step 5: measure the counting register
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
