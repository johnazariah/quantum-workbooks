# Circuit Bench 07: QAOA for MaxCut

## What are we making?

A three-qubit QAOA circuit for **MaxCut on a triangle**.

If you came here from [The $50M Delivery Route](../../blog/posts/bottleneck-01-logistics.md), this is the same teaching example viewed from the Circuit Bench. The blog post explains why a tiny graph belongs in a logistics story. This note does the narrower job: show the actual OpenQASM circuit, explain the gates, and tell you what to expect when you run it.

QAOA is a **variational quantum algorithm**. A quantum circuit prepares a probability distribution over candidate solutions; a classical optimiser chooses the circuit angles that make better solutions more likely. In this circuit note we use fixed angles that are already tuned for the triangle, so you can inspect the circuit without also building the optimiser.

## What you need

- 3 qubits, one per graph node
- Hadamard gates (`h`)
- CNOT gates (`cx`)
- Z-rotations (`rz`)
- X-rotations (`rx`)
- Measurement
- A [Quokka](https://www.quokkacomputing.com/) puck or app

Useful side paths: [Circuit Bench 00 — Reading a Quantum Circuit](../00-reading-a-quantum-circuit/README.md) covers gates, unitary rotations, and measurement bases; [Circuit Bench 01 — Bell State](../01-bell-state/README.md) covers Hadamard, CNOT, and measurement correlation in the first two-qubit example.

## The graph

We use the smallest graph that still shows the QAOA mechanism:

```text
    0
   / \
  /   \
 1-----2
```

The edges are:

```text
(0, 1), (0, 2), (1, 2)
```

A bit string assigns each node to one side of the cut:

```text
0 = one side
1 = the other side
```

An edge is cut if its endpoints have different bits.

| Bit string | Cut value |
|:---:|:---:|
| `000` | 0 |
| `001` | 2 |
| `010` | 2 |
| `011` | 2 |
| `100` | 2 |
| `101` | 2 |
| `110` | 2 |
| `111` | 0 |

The best possible cut value is 2. Six bit strings achieve it; `000` and `111` cut no edges.

## The circuit rhythm

Depth-1 QAOA has four stages:

1. **Prepare all colourings.** Apply Hadamards to create an equal superposition over the eight bit strings.
2. **Apply one phase block per edge.** Use a CNOT-`rz`-CNOT sandwich to add a phase that depends on whether two endpoint bits agree or differ.
3. **Mix neighbouring colourings.** Apply `rx` rotations so amplitude can move between bit strings that differ by one bit.
4. **Measure.** Sample a bit string and score its cut value.

The cost phase alone does not change measurement probabilities. It writes information into phase. The mixer is what lets those phases interfere and change the final probability distribution.

## Parameter convention

OpenQASM 2.0 defines:

$$
R_Z(\theta) = e^{-i\theta Z/2}, \qquad R_X(\theta) = e^{-i\theta X/2}.
$$

This note uses the same convention as the companion notebook:

```text
edge block: cx; rz(2 * gamma); cx
mixer:      rx(2 * beta)
```

For this triangle instance, the fixed angles are:

```text
gamma = 1.264491043069892
beta  = 0.3063052837250049
```

So the QASM uses:

```text
rz(2.528982)
rx(0.612611)
```

Do not treat those numbers as universal QAOA constants. They are good angles for this particular graph and this particular gate convention.

## Step 1: Prepare the search space

```qasm
h q[0];
h q[1];
h q[2];
```

This creates an equal superposition over all eight possible cuts.

## Step 2: Add one edge phase block per edge

For edge `(0, 1)`:

```qasm
cx q[0], q[1];
rz(2.528982) q[1];
cx q[0], q[1];
```

The first CNOT computes the parity of the two endpoint bits into the target qubit. The `rz` gate applies a phase based on that parity. The second CNOT uncomputes the parity so the bit string is restored.

Repeat the same pattern for `(0, 2)` and `(1, 2)`.

## Step 3: Mix

```qasm
rx(0.612611) q[0];
rx(0.612611) q[1];
rx(0.612611) q[2];
```

The mixer lets amplitude flow between neighbouring bit strings. Because the edge blocks have already given different phases to different cut values, this mixing turns hidden phase information into visible probability bias.

## Step 4: Measure

```qasm
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
```

Each shot returns one candidate cut.

## The complete circuit

The full QASM file is [`qaoa_maxcut.qasm`](qaoa_maxcut.qasm):

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

h q[0];
h q[1];
h q[2];

cx q[0], q[1];
rz(2.528982) q[1];
cx q[0], q[1];

cx q[0], q[2];
rz(2.528982) q[2];
cx q[0], q[2];

cx q[1], q[2];
rz(2.528982) q[2];
cx q[1], q[2];

rx(0.612611) q[0];
rx(0.612611) q[1];
rx(0.612611) q[2];

measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
```

![QAOA MaxCut circuit](circuit.png)

## Run it

Paste `qaoa_maxcut.qasm` into Quokka and sample it.

In an ideal simulation with the fixed angles above, the six optimal bit strings are strongly favoured and `000` and `111` are heavily suppressed:

```text
001, 010, 011, 100, 101, 110  -> about one-sixth each
000, 111                      -> close to zero
```

Shot noise means your exact counts will vary. The important thing to check is not the order of the bit strings; it is whether the samples are concentrated on cuts with value 2.

## Deep dive

### Why the CNOT-RZ-CNOT block is a ZZ phase

CNOT computes parity. For two bits $a$ and $b$, the target becomes $a \oplus b$ after the first CNOT.

The `rz` rotation applies one phase when that parity is 0 and another phase when it is 1.

The second CNOT restores the target bit. The computational basis state is unchanged, but it has picked up a phase depending on whether the two endpoint bits agreed or differed.

Algebraically:

$$
\mathrm{CNOT}_{ij}\, R_Z(\theta)_j\, \mathrm{CNOT}_{ij}
=
e^{-i\theta Z_i Z_j/2}.
$$

Setting $\theta = 2\gamma$ gives the edge phase used in this note.

### Where the optimiser went

Full QAOA does not normally start with fixed angles. It runs a loop:

```text
choose gamma, beta
run the circuit many times
estimate the average cut value
update gamma, beta classically
repeat
```

This note freezes the loop at one good pair of angles so the circuit is readable as a standalone QASM program.

The companion notebook runs the same idea in a more workbook-like form: it builds the graph, brute-forces the answer, constructs QASM, samples the circuit, and sweeps the parameter landscape.

## Notes

- **This is a circuit note, not an advantage claim.** The triangle does not need a quantum computer. It is small enough to expose the mechanism.
- **The angles are convention-dependent.** If you change signs, factors of two, or edge-order conventions, the best numerical angles can change.
- **The optimiser is part of QAOA.** This QASM file shows one tuned circuit. The full algorithm is the quantum-classical loop around it.
- **MaxCut is the clean specimen.** Scheduling, routing, and other optimisation problems need more elaborate encodings, but the pattern is the same: turn the objective into phases, mix, measure, and tune.
