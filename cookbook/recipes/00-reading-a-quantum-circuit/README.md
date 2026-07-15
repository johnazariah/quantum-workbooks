# Circuit Bench 00: Reading a Quantum Circuit

## What is this note for?

This is the small amount of circuit literacy the Bottleneck posts assume.

You do not need a quantum mechanics course before reading the workbooks. You do need a working picture of four ideas:

1. A **qubit** is not just a hidden classical bit.
2. A **gate** is a reversible operation on qubits.
3. A **measurement basis** is the question you ask at the end.
4. A **measurement** turns the quantum state into a classical outcome.

The Bloch sphere is the quickest honest picture for a single qubit.

## The Bloch sphere picture

A single qubit state can be pictured as an arrow on a sphere.

```text
                 |0>
                  z
                  |
                  |
        |->  -----+-----  |+>      x
                  |
                  |
                 |1>
```

The north pole is $|0\rangle$. The south pole is $|1\rangle$. Points on the equator are superpositions such as

$$
|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}},
\qquad
|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.
$$

The Bloch sphere is a picture of a **single** qubit. It is useful, but it does not scale to entanglement. Two entangled qubits cannot be fully described by drawing one independent sphere per qubit.

## Gates are unitary rotations

Quantum gates are **unitary** operations. For this note, read that as:

- they are reversible before measurement;
- they preserve total probability;
- on a single qubit, many of them can be pictured as rotations of the Bloch-sphere arrow.

For example, OpenQASM rotation gates use angles:

```qasm
rx(1.570796) q[0];   // rotate around the X axis by pi/2
ry(1.570796) q[0];   // rotate around the Y axis by pi/2
rz(1.570796) q[0];   // rotate around the Z axis by pi/2
```

The Hadamard gate, written `h`, is the common basis-changing gate:

```qasm
h q[0];
```

It maps the ordinary Z-basis states into X-basis states:

$$
H|0\rangle = |+\rangle,
\qquad
H|1\rangle = |-\rangle.
$$

That is why Hadamards appear so often before and after the "interesting" part of a circuit. They change which features of the state will become visible when we measure.

## Measurement is a question in a basis

Hardware measurement in OpenQASM is a Z-basis measurement:

```qasm
measure q[0] -> c[0];
```

That asks:

```text
Is the qubit closer to |0> or |1> along the Z axis?
```

The answer is stored as a classical bit: `0` or `1`.

If the qubit is exactly $|0\rangle$, the answer is always `0`. If it is exactly $|1\rangle$, the answer is always `1`. If it is on the equator, such as $|+\rangle$, a Z-basis measurement gives `0` half the time and `1` half the time.

The important point is that measurement is not passive observation. Measurement chooses a basis, returns a classical outcome, and leaves the post-measurement state consistent with that outcome.

## Measuring in another basis

OpenQASM gives us Z-basis measurement directly. To measure in another basis, rotate the state first, then measure in Z.

For example, an X-basis measurement can be implemented by applying `h` immediately before `measure`:

```qasm
h q[0];
measure q[0] -> c[0];
```

This works because `h` maps the X-axis states back onto the Z-axis states:

```text
|+> --H--> |0>
|-> --H--> |1>
```

So "measure in the X basis" usually means:

```text
change basis with H, then perform the usual measurement
```

## Three tiny circuits

These are deliberately small. They are here to make the vocabulary concrete before Bell states, QAOA, or phase estimation appear.

### 1. Prepare an equator state and measure in Z

The file [`z-basis-of-plus.qasm`](z-basis-of-plus.qasm) prepares $|+\rangle$ and measures it in the ordinary Z basis:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[1];
creg c[1];

h q[0];

measure q[0] -> c[0];
```

Expected result: roughly half `0`, half `1`.

That randomness is not because the circuit forgot what it did. It is because the Z-basis question is the wrong question for distinguishing $|+\rangle$ from $|-\rangle$.

### 2. Prepare the same state and measure in X

The file [`x-basis-of-plus.qasm`](x-basis-of-plus.qasm) prepares the same $|+\rangle$ state, then applies `h` before measurement:

```qasm
h q[0];        // prepare |+>
h q[0];        // rotate X-basis information into the Z basis
measure q[0] -> c[0];
```

Expected result: `0` every time in an ideal noiseless run.

Same state. Different measurement basis. Different information becomes visible.

### 3. Make phase visible

The file [`phase-becomes-visible.qasm`](phase-becomes-visible.qasm) shows why phase matters:

```qasm
h q[0];
rz(3.141593) q[0];
h q[0];

measure q[0] -> c[0];
```

The first `h` prepares $|+\rangle$. The `rz(pi)` changes the relative phase, turning it into $|-\rangle$ up to an irrelevant global phase. The final `h` converts that phase difference into a Z-basis outcome.

Expected result: `1` every time in an ideal noiseless run.

This is the seed of a pattern that appears throughout quantum algorithms: write information into phase, then use later gates to turn phase into measurement probabilities.

## What this shows

- A gate changes the quantum state before measurement.
- A unitary gate is reversible until measurement intervenes.
- A basis is the axis along which you ask the measurement question.
- A Z-basis measurement of a superposition can look random.
- A basis change can reveal information that was invisible in the original basis.
- Phase is not directly visible in one measurement basis, but later gates can make it visible.

## What this does not show

The Bloch sphere is not a full model of many-qubit computation. It is a reliable single-qubit compass, not the whole map. Entanglement, multi-qubit interference, and algorithmic speedups need larger state spaces.

For the next concrete step, read [Circuit Bench 01: The Bell State](../01-bell-state/README.md). That is where one-qubit circuit literacy becomes a two-qubit quantum effect.

