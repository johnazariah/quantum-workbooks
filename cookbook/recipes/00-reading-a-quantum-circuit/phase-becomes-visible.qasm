OPENQASM 2.0;
include "qelib1.inc";

qreg q[1];
creg c[1];

// Prepare |+>, change its relative phase to |->, then rotate that
// phase difference into the Z basis before measurement.
h q[0];
rz(3.141593) q[0];
h q[0];

measure q[0] -> c[0];
