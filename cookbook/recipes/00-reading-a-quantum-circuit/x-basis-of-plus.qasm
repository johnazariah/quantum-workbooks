OPENQASM 2.0;
include "qelib1.inc";

qreg q[1];
creg c[1];

// Prepare |+>.
h q[0];

// Measuring in the X basis is H followed by the usual Z-basis measurement.
h q[0];
measure q[0] -> c[0];
