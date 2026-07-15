# Circuit Bench 01: The Bell State

## What are we making?

Two qubits whose measurement results are correlated because they share one quantum state.

The circuit is tiny:

```qasm
h q[0];
cx q[0], q[1];
```

After those two gates, the qubits are in the Bell state

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}.
$$

If you measure both qubits in the usual computational basis, you should see only `00` and `11`, about half the time each. That is the first visible signature.

It is not the whole story. A classical shared random bit can also produce matching `00`/`11` outcomes. The quantum content of the Bell state is the **coherence** between the two branches, and you see that by changing basis before measurement. This circuit note shows both pieces carefully.

## What you need

- 2 qubits
- 1 Hadamard gate (`h`)
- 1 CNOT gate (`cx`)
- Measurement
- Optional: 2 more Hadamard gates for the X-basis check
- A [Quokka](https://www.quokkacomputing.com/) puck or app

If terms like gate, basis, and measurement are new, start with [Circuit Bench 00: Reading a Quantum Circuit](../00-reading-a-quantum-circuit/README.md). Otherwise, this note is self-contained.

## Step 1: Declare qubits and classical bits

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];
```

The two qubits start in $|00\rangle$.

## Step 2: Put the first qubit in superposition

```qasm
h q[0];
```

The Hadamard turns the first qubit into an equal superposition:

$$
|0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}.
$$

The two-qubit state is now

$$
\frac{|00\rangle + |10\rangle}{\sqrt{2}}.
$$

The first qubit is in superposition; the second is still just $|0\rangle$.

## Step 3: Entangle with CNOT

```qasm
cx q[0], q[1];
```

CNOT flips the target qubit when the control qubit is 1:

```text
|00> -> |00>
|10> -> |11>
```

Because the control qubit is in superposition, both branches are transformed coherently:

$$
\frac{|00\rangle + |10\rangle}{\sqrt{2}}
\xrightarrow{\mathrm{CNOT}}
\frac{|00\rangle + |11\rangle}{\sqrt{2}}.
$$

This is $|\Phi^+\rangle$.

## Step 4: Measure in the Z basis

```qasm
measure q[0] -> c[0];
measure q[1] -> c[1];
```

You should see:

```text
00 about half the time
11 about half the time
01 never, ideally
10 never, ideally
```

This confirms **correlation in the computational basis**.

It does not, by itself, prove non-classicality. A classical source that flips one fair coin and copies the result would also produce only `00` and `11`. To see the difference, we need to ask a second question.

## Optional check: measure in the X basis

To measure in the X basis, apply a Hadamard to each qubit immediately before measurement:

```qasm
h q[0];
h q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
```

For $|\Phi^+\rangle$, the outcomes are again correlated: `00` and `11`.

That is not what a classical 50/50 mixture of `00` and `11` would do. If you took the classical mixture and measured in the X basis, you would get all four outcomes roughly equally. The extra X-basis correlation is evidence that the Bell state is a coherent superposition, not just a hidden coin flip.

This is still not a full Bell test. A Bell test uses several measurement settings and checks a Bell inequality. But the X-basis check is the right next step after the simple `00`/`11` check.

## The complete Z-basis circuit

The file [`bell.qasm`](bell.qasm) contains the simple Z-basis version:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
```

![Bell State circuit](circuit.png)

## Run it

Run `bell.qasm` on Quokka. You should see counts concentrated on `00` and `11`:

```text
{'00': 512, '11': 512}   # idealised example
```

Real shot counts vary, but `01` and `10` should be absent or very rare in a noiseless simulator.

Then try the X-basis version by inserting two Hadamards before measurement. You should again see matching outcomes. That second basis is what tells you there is more here than a copied classical bit.

## Deep dive

### Gate matrices and state evolution

The Hadamard gate is

$$
H = \frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}.
$$

So

$$
H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}.
$$

The CNOT gate flips the target qubit when the control qubit is 1:

```text
|00> -> |00>
|01> -> |01>
|10> -> |11>
|11> -> |10>
```

Therefore:

$$
|00\rangle
\xrightarrow{H \otimes I}
\frac{|00\rangle + |10\rangle}{\sqrt{2}}
\xrightarrow{\mathrm{CNOT}}
\frac{|00\rangle + |11\rangle}{\sqrt{2}}.
$$

### Bell state versus classical mixture

The Bell state is

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}.
$$

A classical mixture with the same Z-basis statistics is:

```text
with probability 1/2: prepare 00
with probability 1/2: prepare 11
```

These look the same if you only measure in the Z basis.

They differ in the X basis. Applying $H$ to both qubits maps:

$$
|\Phi^+\rangle
\mapsto
|\Phi^+\rangle,
$$

so the outcomes are still correlated.

But the classical mixture becomes a mixture of $|++\rangle$ and $|--\rangle$ when written in the X basis, which gives no guaranteed matching bit after Z-basis measurement. Operationally, after the basis-change Hadamards it produces all four bit strings with equal probability.

That is why the second measurement basis matters.

### The four Bell states

The four Bell states are:

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}},
\qquad
|\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}},
$$

$$
|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}},
\qquad
|\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}.
$$

In the Z basis, $|\Phi^+\rangle$ and $|\Phi^-\rangle$ both produce matching outcomes. The relative phase is invisible.

In the X basis, that phase becomes visible:

| State | Z-basis pattern | X-basis pattern |
|---|---|---|
| $\lvert\Phi^+\rangle$ | same | same |
| $\lvert\Phi^-\rangle$ | same | different |
| $\lvert\Psi^+\rangle$ | different | same |
| $\lvert\Psi^-\rangle$ | different | different |

This is why measuring only one basis is not enough to distinguish all four Bell states.

### Bell tests

A full Bell test is stronger than the checks in this circuit note. It measures entangled qubits in several carefully chosen bases and evaluates an inequality, such as the CHSH inequality.

Classical local-hidden-variable theories obey a bound. Quantum mechanics predicts that Bell states can violate it. That violation is the sharp sense in which Bell-state correlations cannot be explained classically.

This note stops earlier: it prepares a Bell state, shows the obvious Z-basis correlation, and then uses an X-basis check to reveal coherence.

## Notes

- **Do not over-read the first histogram.** Seeing only `00` and `11` is the start of the story, not the proof of entanglement.
- **Basis matters.** Relative phase is invisible in the computational basis but visible after a basis change.
- **This is the first reusable primitive.** Bell states are used in teleportation, entanglement swapping, superdense coding, and tests of non-classical correlation.
- **Next natural circuit:** Teleportation, which uses a Bell pair as a resource.
