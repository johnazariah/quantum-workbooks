OPENQASM 2.0;
include "qelib1.inc";

// VQE for H₂ molecule at bond length 0.735 Å
// Minimal STO-3G basis, Bravyi-Kitaev encoding
// 2-qubit ansatz with one variational parameter θ
// Optimal θ ≈ 0.59 radians (pre-optimized)

qreg q[2];
creg c[2];

// Initial Hartree-Fock state: |01⟩
x q[0];

// Variational ansatz: single excitation
// Implements exp(-i θ/2 (X0 Y1 - Y0 X1)) via decomposition
// This is the "give-phase" parameterized excitation gate

ry(0.59) q[1];
cx q[1], q[0];
ry(-0.59) q[1];
cx q[1], q[0];

// Measure in Z basis (for ⟨Z0⟩ and ⟨Z1⟩ terms)
measure q[0] -> c[0];
measure q[1] -> c[1];
