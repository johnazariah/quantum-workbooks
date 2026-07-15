OPENQASM 2.0;
include "qelib1.inc";

// VQE trial circuit for the reduced two-qubit H2 model.
// This file measures one trial angle in the Z basis.

qreg q[2];
creg c[2];

// Hartree-Fock reference state for this qubit ordering.
x q[1];

// One trial point in the variational ansatz.
ry(1.570796) q[0];
cx q[0], q[1];

// Z-basis measurement for Z0, Z1, and Z0Z1 estimates.
measure q[0] -> c[0];
measure q[1] -> c[1];
