# Recipe 02: Quantum Teleportation

## What are we making?

A protocol that transmits the *exact* quantum state of one qubit to another — without physically moving the qubit. Alice has a qubit in some state $|\psi\rangle$. She wants Bob to have that state, but she can't send the qubit itself. Using a shared Bell pair and two classical bits, she can **teleport** $|\psi\rangle$ to Bob's qubit.

This isn't science fiction — it's the backbone of quantum networking, quantum error correction, and measurement-based computation. And it takes only 6 gates.

## Ingredients

- 3 qubits (`q[0]` = Alice's message, `q[1]` = Alice's half of the Bell pair, `q[2]` = Bob's half)
- 1 X gate (`x`)
- 2 Hadamard gates (`h`)
- 2 CNOT gates (`cx`)
- 1 Z gate (`z`)
- Classical-controlled operations (`if`)
- A [Quokka](https://www.quokkacomputing.com/) (puck or app)

**Prerequisites:** [Recipe 01 — Bell State](../01-bell-state/README.md). You should understand entanglement and the Bell state $|\Phi^+\rangle$.

## Background: why can't Alice just copy the qubit?

You might think: if Alice knows the state $|\psi\rangle$, can't she just tell Bob what it is? Or make a copy and send that?

No. Two fundamental theorems forbid it:

1. **No-cloning theorem.** There is no quantum operation that takes an unknown state $|\psi\rangle$ and produces two copies $|\psi\rangle \otimes |\psi\rangle$. This is a consequence of the linearity of quantum mechanics — if you could clone, you could distinguish non-orthogonal states, which violates unitarity.

2. **Measurement destroys.** If Alice measures $|\psi\rangle$ to learn what it is, she collapses it. She gets one classical bit (0 or 1), but the continuous information in the amplitudes $\alpha$ and $\beta$ is lost forever. One measurement can't capture a state from a continuous space.

Teleportation solves this: Alice transfers $|\psi\rangle$ to Bob without ever learning what $|\psi\rangle$ is, and without cloning it. The original is destroyed in the process (as it must be — no-cloning is not violated).

## Method

We'll teleport the state $|1\rangle$ from Alice to Bob. (In the code we use `x q[0]` to prepare this state. You could prepare any state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ — the protocol works the same.)

### Step 1: Prepare the state to teleport

```
x q[0];
```

Alice's qubit `q[0]` is now in state $|1\rangle$. This is her "message" — the state she wants to send to Bob.

The full 3-qubit state is:

$$|1\rangle \otimes |0\rangle \otimes |0\rangle = |100\rangle$$

### Step 2: Create a Bell pair between Alice and Bob

```
h q[1];
cx q[1], q[2];
```

This puts `q[1]` (Alice's half) and `q[2]` (Bob's half) into the Bell state $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$, exactly as in Recipe 01.

The full state is now:

$$|1\rangle \otimes \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = \frac{1}{\sqrt{2}}(|100\rangle + |111\rangle)$$

Alice holds `q[0]` and `q[1]`. Bob holds `q[2]`. They can be in different rooms, different cities — it doesn't matter, as long as the Bell pair was shared in advance.

### Step 3: Alice's Bell measurement

Alice performs a Bell measurement on her two qubits (`q[0]` and `q[1]`):

```
cx q[0], q[1];
h q[0];

measure q[0] -> c0[0];
measure q[1] -> c1[0];
```

The CNOT and Hadamard effectively "undo" the Bell-state creation, projecting Alice's two qubits onto one of the four Bell states. This entangles Alice's message with the shared Bell pair, transferring the quantum information to Bob's qubit.

Let's trace the math. Before Alice's gates, the state is $\frac{1}{\sqrt{2}}(|100\rangle + |111\rangle)$.

After `cx q[0], q[1]` (CNOT with `q[0]` as control, `q[1]` as target):

$$\frac{1}{\sqrt{2}}(|1\mathbf{1}0\rangle + |1\mathbf{0}1\rangle)$$

(The bold digit is `q[1]`, which flipped because the control `q[0]` is $|1\rangle$.)

After `h q[0]` (Hadamard on `q[0]`), recall that $H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$:

$$\frac{1}{2}\Big[(|0\rangle - |1\rangle)|10\rangle + (|0\rangle - |1\rangle)|01\rangle\Big]$$

Expanding:

$$\frac{1}{2}\Big[|010\rangle - |110\rangle + |001\rangle - |101\rangle\Big]$$

Regrouping by Alice's measurement outcomes (first two qubits):

$$\frac{1}{2}\Big[|00\rangle(|1\rangle) + |01\rangle(|0\rangle) - |10\rangle(|1\rangle) - |11\rangle(|0\rangle)\Big]$$

| Alice measures | Bob's qubit becomes | What Bob needs to do |
|:---|:---|:---|
| `00` | $\|1\rangle$ | Nothing — it's already $\|\psi\rangle = \|1\rangle$ |
| `01` | $\|0\rangle$ | Apply $X$ (bit flip) |
| `10` | $-\|1\rangle$ | Apply $Z$ (phase flip) |
| `11` | $-\|0\rangle$ | Apply $Z$ then $X$ |

Alice gets one of four equally likely outcomes. No matter which one, Bob's qubit encodes the original state — possibly with known corrections.

### Step 4: Bob's corrections

Alice sends Bob her two classical measurement bits. Bob applies corrections:

```
if(c1==1) x q[2];
if(c0==1) z q[2];
```

- If Alice's `q[1]` measured 1: Bob applies $X$ (bit flip)
- If Alice's `q[0]` measured 1: Bob applies $Z$ (phase flip)

After these corrections, Bob's qubit `q[2]` is in the state $|1\rangle$ — exactly the state Alice started with.

### Step 5: Verify

```
measure q[2] -> c2[0];
```

Bob measures his qubit to confirm: he should always get `1`.

## The complete circuit

Here's the full QASM file — also available as [`teleport.qasm`](teleport.qasm):

```
OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c0[1];   // Alice's message qubit measurement
creg c1[1];   // Alice's Bell-pair qubit measurement
creg c2[1];   // Bob's qubit measurement (the teleported state)

// Step 1: Prepare the state to teleport — |1⟩
x q[0];

// Step 2: Create a Bell pair between q[1] and q[2]
h q[1];
cx q[1], q[2];

// Step 3: Alice's Bell measurement
cx q[0], q[1];
h q[0];

measure q[0] -> c0[0];
measure q[1] -> c1[0];

// Step 4: Bob's corrections (classically controlled)
if(c1==1) x q[2];
if(c0==1) z q[2];

// Step 5: Measure Bob's qubit
measure q[2] -> c2[0];
```

As a circuit diagram:

```
q[0] (|1⟩) : ── X ─────────────●─── H ─── M ────────────────
                                │                    ║
q[1] (|0⟩) : ────────── H ──●──X──────── M ────────║────────
                             │              ║       ║
q[2] (|0⟩) : ───────────────X─────── if c1: X ── if c0: Z ── M
```

## Taste test

Copy the contents of [`teleport.qasm`](teleport.qasm) and paste it into your Quokka.

You should see Bob's qubit (`c2`) always measure `1`, regardless of what Alice's measurements (`c0`, `c1`) were. The full output has 4 equally likely outcomes:

```
{'0 0 1': 0.25, '0 1 1': 0.25, '1 0 1': 0.25, '1 1 1': 0.25}
```

The last bit (Bob's) is always `1`. The first two bits (Alice's) are uniformly random. This is the hallmark of teleportation: **the message always arrives, regardless of the random measurement outcome**.

**Try it:** Change `x q[0]` to just remove it entirely (teleporting $|0\rangle$ instead). Now Bob should always measure `0`.

## Deep dive

??? abstract "The general case: teleporting an arbitrary state"

    We teleported $|1\rangle$, but the protocol works for *any* state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$.

    Starting from $|\psi\rangle \otimes |\Phi^+\rangle$:

    $$(\alpha|0\rangle + \beta|1\rangle) \otimes \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

    $$= \frac{1}{\sqrt{2}}\Big[\alpha(|000\rangle + |011\rangle) + \beta(|100\rangle + |111\rangle)\Big]$$

    After CNOT (q[0] → q[1]) and Hadamard on q[0], the state becomes:

    $$\frac{1}{2}\Big[|00\rangle(\alpha|0\rangle + \beta|1\rangle) + |01\rangle(\alpha|1\rangle + \beta|0\rangle) + |10\rangle(\alpha|0\rangle - \beta|1\rangle) + |11\rangle(\alpha|1\rangle - \beta|0\rangle)\Big]$$

    So:

    | Alice measures | Bob has | Correction |
    |:---|:---|:---|
    | $00$ | $\alpha\|0\rangle + \beta\|1\rangle$ | $I$ (none) |
    | $01$ | $\alpha\|1\rangle + \beta\|0\rangle$ | $X$ |
    | $10$ | $\alpha\|0\rangle - \beta\|1\rangle$ | $Z$ |
    | $11$ | $\alpha\|1\rangle - \beta\|0\rangle$ | $ZX$ |

    In every case, Bob recovers $|\psi\rangle$ after applying the correction $\{I, X, Z, ZX\}$. The amplitudes $\alpha$ and $\beta$ are perfectly preserved — even though Alice never learned their values.

??? abstract "What teleportation is NOT"

    Common misconceptions:

    **"Faster-than-light communication."** No. Alice's measurement outcomes are random; they carry no information. Bob can't use his qubit until he receives Alice's classical bits — which travel at most at the speed of light. Teleportation respects relativity.

    **"Copying a quantum state."** No. After teleportation, Alice's original qubit is in state $|0\rangle$ or $|1\rangle$ (collapsed by measurement). The state was *transferred*, not copied. No-cloning holds.

    **"Transmitting the qubit itself."** No. What's transmitted is the *state* — the quantum information ($\alpha$, $\beta$). The physical qubit stays with Alice. Bob's qubit (which was in a completely different state before) now carries the information.

    **"Useful only for communication."** Actually, teleportation's biggest application is in quantum computing itself. Measurement-based quantum computation (one-way QC) uses teleportation as its fundamental operation. And quantum error correction codes use teleportation-like circuits to move logical qubits.

??? abstract "The Bell measurement, deconstructed"

    Alice's circuit — CNOT followed by Hadamard — is performing a **Bell measurement**: projecting her two qubits onto the Bell basis $\{|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle\}$.

    Why does CNOT + H do this? Because the Bell-state creation circuit is H + CNOT:

    $$|00\rangle \xrightarrow{H \otimes I} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|0\rangle \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle$$

    The inverse is CNOT + H (since both are self-inverse):

    $$|\Phi^+\rangle \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|0\rangle \xrightarrow{H \otimes I} |00\rangle$$

    So CNOT + H maps each Bell state to a unique computational basis state:

    | Bell state | After CNOT + H | Measurement |
    |:---|:---|:---|
    | $\|\Phi^+\rangle$ | $\|00\rangle$ | `00` |
    | $\|\Phi^-\rangle$ | $\|10\rangle$ | `10` |
    | $\|\Psi^+\rangle$ | $\|01\rangle$ | `01` |
    | $\|\Psi^-\rangle$ | $\|11\rangle$ | `11` |

    This is elegant: you don't need a special "Bell measurement device." You just reverse the Bell creation circuit and measure in the computational basis.

??? abstract "Resource cost and classical communication"

    Teleportation consumes:

    - **1 Bell pair** (shared in advance — the entanglement is "used up")
    - **2 classical bits** of communication (Alice → Bob)
    - **1 qubit of quantum information** transferred

    This is optimal. You can't teleport with fewer than 2 classical bits (proven by Holevo's theorem — one qubit carries at most one classical bit, but the correction requires two bits of choice among $\{I, X, Z, ZX\}$).

    The Bell pair is consumed: after the protocol, q[1] and q[2] are no longer entangled. If Alice wants to teleport another qubit, she needs a fresh Bell pair. This makes entanglement a *resource* — created, distributed, consumed.

    **Superdense coding** is the flip side: given a shared Bell pair, Alice can transmit **2 classical bits** by sending **1 qubit**. Teleportation trades 1 Bell pair + 2 classical bits for 1 qubit of quantum information. Superdense coding trades 1 Bell pair + 1 qubit for 2 classical bits. They're dual protocols.

## Chef's notes

- **Try teleporting different states.** Replace `x q[0]` with `h q[0]` to teleport $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$. Now Bob's measurement should give 50/50. Or use `ry(0.6) q[0]` for an arbitrary superposition.

- **The classical bits are essential.** Remove the `if` corrections and Bob's qubit becomes maximally mixed — completely random, no information. This is why teleportation doesn't violate relativity: without Alice's classical message (which travels at ≤ light speed), Bob has noise.

- **Teleportation in the real world.** Teleportation has been demonstrated over 1,400 km via satellite (Micius, 2017) and across metropolitan fiber networks. It's the building block of a future quantum internet.

- **If you liked this, try:** Recipe 03 (Deutsch-Jozsa) uses the same Hadamard + entanglement tools but for a different purpose: solving a problem faster than any classical algorithm. Recipe 04 (Bernstein-Vazirani) extends the same pattern to discover hidden structure.
