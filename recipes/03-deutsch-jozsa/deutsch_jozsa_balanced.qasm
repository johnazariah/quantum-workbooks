OPENQASM 2.0;
include "qelib1.inc";

// Deutsch-Jozsa algorithm for a 2-bit balanced function
// Oracle: f(x) = x0 XOR x1 (balanced)

qreg q[3];   // q[0], q[1] = input register; q[2] = output (ancilla)
creg c[2];   // measure input register only

// Step 1: Put ancilla in |−⟩ state
x q[2];
h q[2];

// Step 2: Put input qubits in superposition
h q[0];
h q[1];

// Step 3: Oracle for f(x) = x0 XOR x1
// Flip ancilla if x0=1, flip again if x1=1
// Net effect: ancilla flipped iff x0 ≠ x1
cx q[0], q[2];
cx q[1], q[2];

// Step 4: Apply Hadamard to input register
h q[0];
h q[1];

// Step 5: Measure input register
measure q[0] -> c[0];
measure q[1] -> c[1];
