OPENQASM 2.0;
include "qelib1.inc";

// Quantum Counting: estimate number of solutions to a search problem
// Using Grover oracle for |11⟩ on 2-qubit search space (N=4, M=1)
// 2 counting qubits for phase estimation

qreg q[4];   // q[0..1] = counting register; q[2..3] = search register
creg c[2];   // measure counting register

// Step 1: Hadamard on all qubits
h q[0];
h q[1];
h q[2];
h q[3];

// Step 2: Controlled-Grover iterations
// Controlled-G^1 from q[1] (least significant counting qubit)
// Grover iteration = Oracle · Diffusion

// -- Controlled Oracle: mark |11⟩ in search register, controlled by q[1] --
// Controlled-CZ on q[2],q[3] controlled by q[1]
// Decompose as: ccx(q[1], q[2], temp) then cz, but simplified:
// Use Toffoli + phase approach
ccx q[1], q[2], q[3];
cz q[1], q[3];
ccx q[1], q[2], q[3];

// -- Controlled Diffusion --
// Diffusion = H X (CZ) X H on search register, controlled by q[1]
h q[2];
h q[3];
x q[2];
x q[3];
ccx q[1], q[2], q[3];
cz q[1], q[3];
ccx q[1], q[2], q[3];
x q[2];
x q[3];
h q[2];
h q[3];

// Controlled-G^2 from q[0] (most significant counting qubit)
// First Grover iteration controlled by q[0]
ccx q[0], q[2], q[3];
cz q[0], q[3];
ccx q[0], q[2], q[3];
h q[2];
h q[3];
x q[2];
x q[3];
ccx q[0], q[2], q[3];
cz q[0], q[3];
ccx q[0], q[2], q[3];
x q[2];
x q[3];
h q[2];
h q[3];

// Second Grover iteration controlled by q[0]
ccx q[0], q[2], q[3];
cz q[0], q[3];
ccx q[0], q[2], q[3];
h q[2];
h q[3];
x q[2];
x q[3];
ccx q[0], q[2], q[3];
cz q[0], q[3];
ccx q[0], q[2], q[3];
x q[2];
x q[3];
h q[2];
h q[3];

// Step 3: Inverse QFT on counting register
swap q[0], q[1];
h q[0];
cp(-1.5708) q[1], q[0];
h q[1];

// Step 4: Measure counting register
measure q[0] -> c[0];
measure q[1] -> c[1];
