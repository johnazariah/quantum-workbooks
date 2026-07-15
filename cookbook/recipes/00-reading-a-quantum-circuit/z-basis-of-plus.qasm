OPENQASM 2.0;
include "qelib1.inc";

qreg q[1];
creg c[1];

// Prepare |+> = (|0> + |1>) / sqrt(2).
h q[0];

// Ask the Z-basis question: |0> or |1>?
measure q[0] -> c[0];
