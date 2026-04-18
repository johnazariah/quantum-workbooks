OPENQASM 2.0;
include "qelib1.inc";

// Grover's algorithm for 3 qubits
// Search target: |101⟩ (decimal 5)

qreg q[3];
creg c[3];

// Step 1: Superposition
h q[0];
h q[1];
h q[2];

// === Grover iteration 1 ===

// Oracle: mark |101⟩ with a phase flip
// Flip phase of |101⟩: need q[0]=1, q[1]=0, q[2]=1
x q[1];              // flip q[1] so we can use a triple-controlled Z
h q[2];
ccx q[0], q[1], q[2];  // Toffoli = CCX
h q[2];
x q[1];              // unflip q[1]

// Diffusion operator: 2|ψ⟩⟨ψ| - I
h q[0];
h q[1];
h q[2];
x q[0];
x q[1];
x q[2];
h q[2];
ccx q[0], q[1], q[2];
h q[2];
x q[0];
x q[1];
x q[2];
h q[0];
h q[1];
h q[2];

// === Grover iteration 2 ===

// Oracle
x q[1];
h q[2];
ccx q[0], q[1], q[2];
h q[2];
x q[1];

// Diffusion
h q[0];
h q[1];
h q[2];
x q[0];
x q[1];
x q[2];
h q[2];
ccx q[0], q[1], q[2];
h q[2];
x q[0];
x q[1];
x q[2];
h q[0];
h q[1];
h q[2];

// Measure
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
