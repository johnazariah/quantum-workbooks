OPENQASM 2.0;
include "qelib1.inc";

// Quantum Phase Estimation for the T gate
// T|1⟩ = e^(iπ/4)|1⟩, so phase φ = 1/8
// Using 3 counting qubits → resolution 1/8

qreg q[4];   // q[0..2] = counting register; q[3] = eigenstate
creg c[3];   // measure counting register

// Step 1: Prepare eigenstate |1⟩
x q[3];

// Step 2: Hadamard on counting register
h q[0];
h q[1];
h q[2];

// Step 3: Controlled-U^(2^k) operations
// U = T gate, eigenvalue e^(2πi·1/8)
// Controlled-T^1 from q[2]
cp(0.7854) q[2], q[3];        // T = phase(π/4)

// Controlled-T^2 from q[1]
cp(1.5708) q[1], q[3];        // T^2 = S = phase(π/2)

// Controlled-T^4 from q[0]
cp(3.14159) q[0], q[3];       // T^4 = Z = phase(π)

// Step 4: Inverse QFT on counting register
// Swap q[0] and q[2]
swap q[0], q[2];

// Inverse QFT gates (reversed order, negative phases)
h q[0];
cp(-1.5708) q[1], q[0];
h q[1];
cp(-0.7854) q[2], q[0];
cp(-1.5708) q[2], q[1];
h q[2];

// Step 5: Measure counting register
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
