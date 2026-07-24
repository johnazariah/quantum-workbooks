---
date: 2026-07-28
notebook: https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/01-logistics.ipynb
categories:
- The Quantum Bottleneck
- Optimisation
tags:
- QAOA
- MaxCut
- combinatorial optimisation
authors:
- John Azariah
social:
  linkedin: 'A delivery company''s route optimisation is worth tens of millions a year. The notebook solves a triangle. That gap is the point. This is the first post in The Quantum Bottleneck, an eight-part series that takes real-world problems, codes up the smallest quantum version that actually runs, and asks honestly: where is the bottleneck, and does a quantum computer help? First up: logistics and QAOA.


    #QuantumComputing #Logistics'
  bluesky: 'New series: The Quantum Bottleneck. Eight real-world problems, each with a runnable notebook. Post 1: logistics route optimisation. The notebook solves a triangle. The problem is worth $50M. That gap is the point.'
---

# The $50M Delivery Route

The notebook starts with a triangle.

The problem starts with trucks.

That gap is the point.

This post is about crossing that gap carefully. The triangle is not a substitute for the logistics problem; it is the smallest example that lets us see the whole mechanism without hiding the important pieces behind software.

<!-- more -->

If you ask a delivery company for the best route through a hundred stops, nobody in the room says, "Great, let's enumerate all possible routes." The exact program is easy to imagine and hopeless to run at that scale. Try every ordering, compute every distance, keep the shortest. Beautiful, correct, and almost immediately impractical.

This is the first lesson of optimisation: the code can be simple while the search space is absurd.

UPS made this painfully concrete. Their ORION route-optimisation system reportedly saved up to **$50 million per year** for each mile shaved from a driver's daily route.[^ups-orion] One mile. Not a perfect route. Not a proof of optimality. One mile, multiplied by a fleet large enough for the arithmetic to become real money.

That is why this matters. We are not optimising because computer scientists enjoy suffering. We are optimising because small improvements in large systems compound.

The notebook does not begin with vehicle routing. It begins with **MaxCut** on a triangle: three nodes, three edges, colour each node one of two colours, and count how many edges connect different colours.

That may feel much smaller than the problem we started with. It is meant to. A triangle is small enough that we can see every possible answer, every circuit operation, and every measurement outcome. It is a microscope slide, not a destination.

## The shape under the logistics

The travelling-salesman problem, vehicle routing, nurse rostering, circuit placement, portfolio selection, and MaxCut all share a shape:

1. There are many discrete decisions.
2. The value of one decision depends on other decisions.
3. You can score any one proposed answer.
4. You cannot score every proposed answer once the instance gets large.

For MaxCut, the decisions are wonderfully bare. Each graph node gets a bit:

```text
0 = one side of the cut
1 = the other side of the cut
```

An edge is "cut" when its endpoints have different bits. So for a triangle with nodes `0`, `1`, and `2`, the bit string `001` means nodes 0 and 1 are on one side, node 2 is on the other. Two of the three edges cross the cut, so the cut value is 2.

There are only eight bit strings for a triangle:

```text
000  001  010  011  100  101  110  111
```

The notebook starts by brute-forcing all of them. This is not because brute force is clever. It is because, for three nodes, brute force is honest. We can see the whole space, compute the truth, and then check whether the quantum circuit is doing anything meaningful.

For a triangle, the best possible cut value is 2. You cannot cut all three edges because a triangle has an odd cycle: once two edges cross the cut, the third edge necessarily lands inside one side. So the six bit strings with one bit different from the other two are optimal; `000` and `111` are the bad ones.

Already we have the core of the lesson:

```text
bit string -> candidate solution
cut value  -> score
best score -> optimisation target
```

The quantum computer does not change the problem. It changes how we try to bias ourselves toward good candidates.

If circuit words like gate, basis, or measurement are new, start with [Circuit Bench 00: Reading a Quantum Circuit](../../circuit-bench/00-reading-a-quantum-circuit/README.md). If you want the first two-qubit example before the QAOA circuit appears, [Circuit Bench 01: The Bell State](../../circuit-bench/01-bell-state/README.md) is the side path: Hadamard, CNOT, measurement correlation, and why changing measurement basis matters. You do not need either note first, but they are there when those primitives deserve a closer look.

## What superposition does not do by itself

The phrase you will hear, usually with great confidence, is:

> A quantum computer tries all answers at once.

There is a useful intuition hiding inside that sentence, but by itself it points in the wrong direction.

It is true that the QAOA circuit begins by placing the qubits into a superposition of all eight triangle colourings. But if you created that superposition and immediately measured it, you would just get a random bit string. You would not have solved MaxCut. You would have used quantum hardware to sample uniformly from the candidate answers.

So superposition is necessary, but not sufficient.

The useful word is **interference**.

A quantum algorithm is useful when it arranges the computation so that unwanted possibilities cancel and wanted possibilities reinforce. The possibilities being "present" is not enough. Their amplitudes have to be made to interfere in the right way before measurement.

QAOA, the **Quantum Approximate Optimisation Algorithm**, is one attempt to do that for optimisation problems. It does not guarantee the optimum. It does not make NP-hardness evaporate. It produces a probability distribution over candidate answers, and the hope is that good answers appear more often than they would under blind random sampling.

That sounds modest because it is modest. It is also the honest claim, and it is the claim the notebook is designed to make visible.

## The Hamiltonian move

QAOA works by making an optimisation problem look like a physics problem.

In physics, a Hamiltonian assigns energy to states of a system. Low-energy states are special because physical systems tend to settle there. In optimisation, we can borrow the same language: define an artificial energy function where better answers have better energy, then build a quantum circuit that tries to steer probability toward those states.

For MaxCut, the key operator is Pauli-$Z$.

You only need one fact about it:

```text
Z on |0> gives +1
Z on |1> gives -1
```

Now look at an edge between nodes `i` and `j`.

If the two bits are the same, $Z_i Z_j$ gives $+1$.

If the two bits are different, $Z_i Z_j$ gives $-1$.

So this little expression:

$$
\frac{1 - Z_i Z_j}{2}
$$

is exactly an edge-cut detector. It evaluates to 0 when the edge is not cut, and 1 when it is cut.

Sum that expression over every edge and you have turned the graph into an operator:

$$
C = \sum_{(i,j)\in E} \frac{1 - Z_i Z_j}{2}.
$$

Here $C$ is a score to maximise, not an energy to minimise. If you prefer the ground-state language, use $-C$ as the Hamiltonian. The circuit only needs a consistent phase convention.

That is the structural move. A graph problem has become a Hamiltonian. A candidate colouring has become a quantum basis state. The cut value has become something the circuit can imprint as phase.

If you take one idea from this first notebook, make it this:

> QAOA starts by finding the shape of the classical problem and encoding that shape as an operator.

This is the pattern that will come back in the later workbooks. Molecules become Hamiltonians. Schedules become Hamiltonians. Materials become Hamiltonians. The domain vocabulary changes; the structural move keeps reappearing.

## What the circuit actually does

The notebook builds a depth-1 QAOA circuit for the triangle. Depth 1 means one round of the two QAOA moves:

```text
cost, then mix
```

There are four stages in the circuit.

### 1. Start with every colouring equally likely

The circuit begins with Hadamard gates:

```qasm
h q[0];
h q[1];
h q[2];
```

Each Hadamard takes a qubit that starts as `0` and puts it into an equal superposition of `0` and `1`. Three Hadamards on three qubits creates an equal superposition of the eight possible colourings.

At this point, every bit string has probability $1/8$.

Nothing has been optimised yet. We have only prepared the search space.

### 2. Imprint the cost as phase

For each graph edge, the notebook emits the same three-gate pattern:

```qasm
cx q[i], q[j];
rz(2 * gamma) q[j];
cx q[i], q[j];
```

This is the smallest piece of useful machinery in the notebook, so it is worth slowing down.

The first CNOT computes whether the two endpoint bits agree or differ, storing that parity temporarily in the target qubit. The $R_Z$ rotation then applies a phase depending on that parity. The second CNOT uncomputes the parity so the qubits go back to representing the original colouring.

The visible bit string is unchanged.

The phase is changed.

That distinction matters. After the cost step, the probabilities are still not better. If you measured immediately, you would still see a uniform distribution. The cost step has written information in a place measurement cannot directly see.

This is why "try all answers at once" is incomplete. The hard part is not placing answers in superposition. The hard part is arranging the phases so that the next step can turn hidden cost information into visible probability bias.

### 3. Mix neighbouring colourings

The mixer applies an $R_X$ rotation to every qubit:

```qasm
rx(2 * beta) q[0];
rx(2 * beta) q[1];
rx(2 * beta) q[2];
```

An $R_X$ rotation partially moves amplitude between `0` and `1` on a qubit. On the full bit string, that means amplitude can flow between colourings that differ by one bit flip.

This is the quantum analogue of "try a neighbouring solution" in a local search algorithm, but with one crucial difference: the movement is coherent. The amplitudes carry the phases from the cost step. When amplitude arrives from different neighbouring colourings, those phase arrows can add or cancel.

For the triangle, that interference suppresses `000` and `111`, the two colourings that cut no edges, and amplifies the six colourings that cut two edges. The circuit is not inspecting each answer and choosing the best one. The cost phase and mixer have been arranged so that amplitudes interfere differently around good and bad colourings.

### 4. Measure, score, repeat

At the end, the circuit measures:

```qasm
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
```

A single run gives one bit string. That is all measurement ever gives you.

So the notebook runs the circuit many times, counts the observed bit strings, computes the cut value for each one, and estimates the expected cut value of the distribution.

This is the right way to think about QAOA:

```text
one shot       -> one candidate solution
many shots     -> an empirical distribution
cut function   -> score each sample
average score  -> quality of the chosen angles
```

The two angles, $\gamma$ and $\beta$, are the knobs. $\gamma$ controls how strongly the cost information is written into phase. $\beta$ controls how strongly the mixer moves amplitude between neighbouring bit strings. Choose them badly and the circuit is mostly random. Choose them well and the distribution leans toward better answers.

For the same circuit viewed directly on the Circuit Bench, see [QAOA for MaxCut](../../circuit-bench/07-qaoa-maxcut/README.md). The post you are reading explains why this circuit belongs in the logistics story; the Circuit Bench note is the more direct gate-by-gate version.

## Walking through the notebook

Open the notebook here:

[Unit 1 notebook: QAOA for MaxCut](https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/01-logistics.ipynb)

The notebook is deliberately small and explicit. That is not a lack of sophistication; it is the teaching choice. You should be able to see every moving part.

### Section 1: Define the graph

The graph is the triangle:

```python
n_qubits = 3
edges = [(0, 1), (0, 2), (1, 2)]
```

Then the notebook defines the scoring function:

```python
def cut_value(bitstring: str, edges: list) -> int:
    return sum(1 for i, j in edges if bitstring[i] != bitstring[j])
```

This is the classical problem, with no quantum mechanics anywhere near it. Given a proposed colouring, count the edges whose endpoints differ.

The notebook then enumerates all eight bit strings. This gives us ground truth before we run the quantum circuit. That habit is important. On a tiny example, never trust a fancy method before checking it against the boring exact answer.

### Section 2: Build the QAOA circuit

The function `qaoa_qasm` writes OpenQASM 2.0 as a string.

That may look low-level if you are used to polished SDKs, but it is exactly what we want pedagogically. The code does not hide the circuit behind a library object. You can see:

- the Hadamards that prepare the uniform superposition;
- one CNOT-$R_Z$-CNOT block per edge;
- one $R_X$ mixer rotation per qubit;
- the final measurements.

The notebook uses fixed, pre-optimised parameters for the triangle:

```python
gamma_opt = 1.264491043069892
beta_opt = 0.3063052837250049
```

These are not magic constants. They are simply good angles for this small instance. The later parameter sweep shows why angle choice matters.

### Section 3: Run on Quokka

The notebook sends the QASM program to a cloud Quokka and receives measurement counts.

The interesting output is not just "did we get the best bit string?" There are six best bit strings for the triangle, all with cut value 2. The question is whether the circuit shifts probability mass toward those six and away from `000` and `111`.

The bar chart colours optimal outcomes differently from suboptimal ones. This is the moment where the circuit becomes more than a diagram: you can see the distribution produced by interference.

The notebook then computes:

```python
expected_cut = sum(
    cut_value(k, edges) * results[k] / total_shots
    for k in results
)
```

That expected cut value is the quantity the classical optimiser would try to improve in a full QAOA workflow.

### Section 4: Sweep the parameter landscape

This is my favourite part of the notebook, because it makes the hybrid nature of QAOA visible.

The circuit has two knobs: $\gamma$ and $\beta$. The notebook runs a grid of circuits over those angles and records the expected cut value at each grid point. The heatmap is the optimisation landscape.

For a real problem, you would not sweep every point. You would call a classical optimiser. But the sweep is the right teaching move because it shows what the optimiser is trying to navigate.

This is the full hybrid loop in miniature:

```text
choose angles
run quantum circuit
measure samples
compute average cut value
choose better angles
repeat
```

The quantum circuit does not replace classical optimisation. It becomes the thing the classical optimiser queries.

That distinction will matter again in the VQE workbook. QAOA and VQE look like different algorithms, but structurally they are cousins: parameterised quantum circuit inside, classical optimiser outside.

### Section 5: Compare with random sampling

The final comparison is intentionally humble. It asks: what if we simply sampled random colourings?

For a triangle, random sampling is not a strawman. There are only eight states, six of them optimal, so even blind luck does reasonably well. That is another reason this notebook is honest: it does not pretend the tiny graph needs quantum help.

The point is the mechanism. We built a circuit whose distribution is shaped by the objective function, and we checked that it improves on an uninformed baseline for this instance.

That is enough for a first workbook.

Not because the triangle is industrially important.

Because the triangle lets you inspect the entire pipeline.

## What this shows, and what it does not

This notebook does not prove that quantum computers will optimise delivery fleets.

It does not prove that QAOA beats the best classical algorithms.

It does not even prove that depth-1 QAOA is a good idea for large MaxCut instances.

That is not a problem with the notebook. It is the reason the notebook is kept honest.

What it demonstrates is smaller and more useful:

1. A combinatorial optimisation problem can be encoded as a Hamiltonian.
2. The Hamiltonian can be compiled into circuit operations.
3. The cost can be written into quantum phase.
4. A mixer can turn phase differences into measurement bias.
5. Samples from the circuit can be scored classically.
6. A classical optimiser can use those scores to tune the quantum circuit.

That is the QAOA architecture.

The open question is whether this architecture becomes practically useful at the scales and depths where industrial optimisation lives. Today's hardware is noisy and shallow. Classical optimisation is extremely strong. Low-depth QAOA is not a shortcut around decades of optimisation research. The honest research programme is to compare against serious classical baselines, on problem families where the quantum circuit has a structural reason to help, at depths hardware can eventually support.

The triangle is not the destination. It is the first clean specimen under the glass.

## What to try next

If you run the notebook, do not just run it top to bottom and close the tab. Change it.

Change the graph:

```python
n_qubits = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
```

Change $\gamma$ and $\beta$ and watch the distribution flatten or sharpen.

Increase the parameter-sweep resolution and see how noisy the heatmap becomes when each circuit uses fewer shots.

Then extend the QASM builder to depth 2: cost, mixer, cost, mixer, with four angles instead of two. You will immediately feel the tradeoff that defines near-term quantum algorithms: deeper circuits are more expressive, but they are harder to tune and more vulnerable to noise.

That is where the real story starts to become visible.

The larger Quantum Bottleneck project goes further into the logistics motivation and the QAOA advantage debate. The workbook gives you the thing you can touch: a graph, a Hamiltonian, a circuit, a sampler, and a distribution that is no longer uniform.

For a first workbook, that is enough: one triangle, fully exposed.

[^ups-orion]: See the ORION case summary in Delen, ["Analytics Success Story: UPS's ORION Project"](https://www.informit.com/articles/article.aspx?p=2992600&seqNum=6), which reports that reducing one mile per driver per day over a year can save UPS up to $50 million.

Next up: [The Trapdoor](bottleneck-02-cryptography.md) — where the bottleneck is not a search landscape but a hidden period, and the quantum move changes from "cost and mix" to "Fourier and measure."
