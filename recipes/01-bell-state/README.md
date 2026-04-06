# Recipe 01: The Bell State

## What are we making?

Two qubits that are perfectly correlated — measure one, and you instantly know the other, no matter how far apart they are. This is **entanglement**, the resource that makes quantum teleportation, superdense coding, and most quantum algorithms possible.

It's also the simplest interesting quantum circuit you can build: two gates, two qubits, and a result that has no classical explanation.

## Ingredients

- 2 qubits
- 1 Hadamard gate (`h`)
- 1 CNOT gate (`cx`)
- [quokka](https://github.com/XXX/quokka) installed

No prior quantum knowledge required. We'll explain everything as we go.

## Background: what does "correlated" mean here?

Flip two classical coins independently. Sometimes they match, sometimes they don't — about 50/50. You could also *cheat* and glue them together so they always match, but then there's no randomness: you know the outcome before you look.

A Bell state gives you **both**: each individual qubit is perfectly random (50% chance of 0 or 1), but they are *always* correlated (both 0 or both 1). This combination — local randomness with perfect global correlation — is impossible classically. It's the signature of entanglement.

## Method

### Step 1: Declare your qubits

Every QASM 2.0 program starts by saying what version of the language we're using and how many qubits and classical bits we need:

```
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];   // two qubits, both start in state |0⟩
creg c[2];   // two classical bits to store measurement results
```

Both qubits begin in the $|0\rangle$ state. Think of them as two coins, both heads-up.

### Step 2: Create superposition on the first qubit

Apply a **Hadamard gate** to qubit 0:

```
h q[0];
```

This puts qubit 0 into an equal superposition of $|0\rangle$ and $|1\rangle$:

$$|0\rangle \xrightarrow{H} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$

If you measured right now, you'd get 0 or 1 with equal probability. The coin is spinning in the air.

The two-qubit state is now:

$$\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)$$

The qubits are still independent — knowing one tells you nothing about the other.

### Step 3: Entangle with a CNOT

Apply a **CNOT** (controlled-NOT) gate, with qubit 0 as control and qubit 1 as target:

```
cx q[0], q[1];
```

CNOT flips the target qubit *if and only if* the control qubit is $|1\rangle$. Since qubit 0 is in superposition, both possibilities happen:

- The $|00\rangle$ branch: control is 0, target stays 0 → $|00\rangle$
- The $|10\rangle$ branch: control is 1, target flips to 1 → $|11\rangle$

The state is now:

$$\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

This is the **Bell state** $|\Phi^+\rangle$. The qubits are no longer independent. There is no way to write this state as "qubit 0 is in some state AND qubit 1 is in some state" — they are entangled.

### Step 4: Measure

```
measure q[0] -> c[0];
measure q[1] -> c[1];
```

Measurement collapses the superposition. You'll get either `00` or `11`, each with 50% probability. Never `01`, never `10`.

## The complete circuit

Here's the full QASM file — also available as [`bell.qasm`](bell.qasm):

```
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
```

As a circuit diagram:

```
q[0] : ─── H ───●─── M ───
                 │
q[1] : ─────────X─── M ───
```

## Taste test

Run it:

```bash
quokka recipes/01-bell-state/bell.qasm
```

You should see something like:

```
{'00': 0.5, '11': 0.5}
```

Or, if quokka samples shots:

```
{'00': 512, '11': 488}
```

The exact counts vary (it's random!), but you should see *only* `00` and `11`. If you ever see `01` or `10`, something is wrong.

## Chef's notes

- **Why not just use a classical random number generator?** You could generate two identical random bits classically — but you'd need to either (a) decide the value in advance and copy it, or (b) communicate between the bits. A Bell state has neither: the value is undetermined until measurement, yet always correlated. This distinction matters for cryptography (Bell tests) and is the basis of quantum key distribution.

- **The other Bell states.** There are four Bell states total. You can reach any of them by adding a single gate before the Hadamard. We'll use them all in Recipe 02 (Teleportation).

  | State | Circuit | Result |
  |-------|---------|--------|
  | $\|\Phi^+\rangle$ | `h, cx` | `00` + `11` |
  | $\|\Phi^-\rangle$ | `x, h, cx` | `00` - `11` |
  | $\|\Psi^+\rangle$ | `h, cx, x` on target | `01` + `10` |
  | $\|\Psi^-\rangle$ | `x, h, cx, x` on target | `01` - `10` |

- **If you liked this, try:** Recipe 02 (Teleportation) uses Bell states to transmit quantum information. Recipe 03 (Deutsch-Jozsa) uses the same H + entanglement pattern to solve a problem faster than any classical algorithm.
