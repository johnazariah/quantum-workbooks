# Circuit Bench 08: VQE for H2

This note shows the circuit-level core of a Variational Quantum Eigensolver (VQE) calculation for a reduced two-qubit model of the hydrogen molecule.

It is not a full chemistry pipeline. The molecular Hamiltonian has already been reduced to qubit operators, and the circuit below is one trial state in the variational loop. The goal is to make the moving parts visible: state preparation, a parameterised ansatz, basis changes, measurement, and energy reconstruction.

## What this circuit does

VQE tries to estimate the ground-state energy of a Hamiltonian $H$. For a trial state $|\psi(\theta)\rangle$, the variational principle says

$$
\langle \psi(\theta) | H | \psi(\theta) \rangle \geq E_0,
$$

where $E_0$ is the true ground-state energy. A classical optimiser changes $\theta$; the quantum device prepares the state and measures the terms needed to estimate the energy.

For the reduced H2 model used in the companion notebook, the Hamiltonian has the form

$$
H =
g_0 I
+ g_1 Z_0
+ g_2 Z_1
+ g_3 Z_0 Z_1
+ g_4 X_0 X_1
+ g_5 Y_0 Y_1 .
$$

That means one circuit run is not enough. The $Z$ terms, $X_0X_1$ term, and $Y_0Y_1$ term are estimated with different measurement bases and then combined with the coefficients.

## Circuit walkthrough

The public QASM file, [`vqe_h2_zz.qasm`](vqe_h2_zz.qasm), shows the $Z$-basis measurement circuit for one trial angle.

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// Hartree-Fock reference state for this qubit ordering
x q[1];

// One trial point in the variational ansatz
ry(1.570796) q[0];
cx q[0], q[1];

// Z-basis measurement
measure q[0] -> c[0];
measure q[1] -> c[1];
```

The first line after the registers prepares the reference occupation pattern used by the reduced model. The `ry` rotation introduces the variational parameter. The `cx` entangles the two qubits so the trial state can mix two occupation patterns rather than staying a single classical bit string.

For a full energy estimate, run related circuits with basis rotations before measurement:

| Term | Basis rotation before measurement | What the counts estimate |
|---|---|---|
| $Z_0$, $Z_1$, $Z_0Z_1$ | none | occupation-basis expectations |
| $X_0X_1$ | `h` on both qubits | correlation in the $X$ basis |
| $Y_0Y_1$ | `sdg` then `h` on both qubits | correlation in the $Y$ basis |

This is why VQE is a measurement workflow, not just a single pretty circuit diagram.

## Run it

Run `vqe_h2_zz.qasm` on a simulator or compatible OpenQASM 2.0 runner. In the displayed `q[0] q[1]` order, the trial angle in this file should put most of the probability on the two occupation patterns `01` and `10`.

For 1024 ideal shots, a typical result is approximately:

```text
{'01': 512, '10': 512}
```

Shot noise will move the counts around. The important feature is that the circuit is no longer a single Hartree-Fock bit string; the ansatz has created a superposition that can be tested in several measurement bases.

## What this shows

This small circuit shows the core VQE mechanics:

- a molecule becomes a qubit Hamiltonian;
- a parameterised circuit prepares a trial state;
- basis rotations turn different Pauli terms into measurable $Z$-basis counts;
- the measured expectations are combined into an energy;
- a classical optimiser repeats the process for new angles.

It also shows why VQE felt plausible for early hardware: the circuit can be shallow, while the expensive search is shared with a classical optimiser.

## What this does not show

This is not a scalable drug-discovery calculation. It does not generate molecular integrals, choose an active space, scan bond lengths, or optimise a production ansatz. It also does not remove the measurement problem: larger molecular Hamiltonians can contain many Pauli terms, and each term needs enough shots to be useful.

Treat this as the smallest bench-top version of the idea. The companion Bottleneck notebook uses the same structure to sweep a parameter and compare the measured energy against exact diagonalisation of the reduced model.
