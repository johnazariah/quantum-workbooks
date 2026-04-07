OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c0[1];   // Alice's message qubit measurement
creg c1[1];   // Alice's Bell-pair qubit measurement
creg c2[1];   // Bob's qubit measurement (the teleported state)

// Step 1: Prepare the state to teleport — |1⟩
x q[0];

// Step 2: Create a Bell pair between q[1] and q[2]
h q[1];
cx q[1], q[2];

// Step 3: Alice's Bell measurement
cx q[0], q[1];
h q[0];

measure q[0] -> c0[0];
measure q[1] -> c1[0];

// Step 4: Bob's corrections (classically controlled)
if(c1==1) x q[2];
if(c0==1) z q[2];

// Step 5: Measure Bob's qubit
measure q[2] -> c2[0];
