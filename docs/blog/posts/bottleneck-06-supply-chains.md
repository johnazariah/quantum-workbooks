---
date: 2026-08-15
notebook: https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/06-supply-chains.ipynb
categories:
- The Quantum Bottleneck
- Supply Chains
tags:
- QAOA
- QUBO
- scheduling
- logistics
- combinatorial optimisation
authors:
- John Azariah
social:
  linkedin: 'Assign nurses to shifts. Route trucks through depots. Match jobs to machines. These are not smooth optimisation problems; they are combinatorial, and a decision is yes or no. QAOA encodes them as QUBO problems and searches for the optimal assignment. This post walks through the encoding, the circuit, and the gap between satisfying a few constraints and solving a real scheduling problem.


    #QuantumComputing #Optimisation'
  bluesky: 'Bottleneck 06: The Scheduling Nightmare. Supply chains are webs of discrete choices. QAOA attacks them as QUBO problems. The post walks through the gap between a toy schedule and a real one.'
---

# The Scheduling Nightmare

**A supply chain is a web of discrete choices. The hard part is not writing down one constraint; it is satisfying many constraints at once without losing the objective you actually care about.**

<!-- more -->

Assign nurses to shifts. Route trucks through depots. Place inventory across warehouses. Match jobs to machines. Decide which supplier gets which order when demand, capacity, timing, and penalties all interact.

These are not smooth optimisation problems where a small nudge gives a small improvement. They are combinatorial. A decision is often yes or no, route A or route B, nurse 1 or nurse 2, shift covered or uncovered.

That discreteness is why supply-chain optimisation becomes difficult so quickly.

## The bottleneck: too many assignments

Take a tiny staffing problem. Suppose $x_{ij}$ is a binary variable that says whether nurse $i$ works shift $j$. Even before preferences, overtime, skill mixes, legal rest periods, and fairness rules enter the model, the number of possible assignments grows exponentially with the number of binary choices.

The standard optimisation move is to turn those choices into an objective function. Reward useful assignments, penalise broken constraints, and search for the bitstring with the lowest cost.

One common form is a QUBO: a **quadratic unconstrained binary optimisation** problem,

$$
C(x) = x^T Q x,
$$

where $x$ is a vector of bits and $Q$ encodes both the objective and the penalties. "Unconstrained" does not mean the original problem had no constraints. It means the constraints have been folded into the cost function as penalties.

That is powerful, but it creates a new engineering problem: if the penalties are too small, the optimiser may prefer infeasible schedules; if they are too large, the real objective gets drowned out.

## The quantum idea: turn the cost into a circuit

Gate-based quantum optimisation usually starts by mapping the QUBO to an Ising Hamiltonian. Binary variables become spin variables, and the cost function becomes an energy landscape.

QAOA, the Quantum Approximate Optimisation Algorithm, then alternates two operations:

1. a **phase separator** that gives each bitstring a phase depending on its cost;
2. a **mixer** that moves amplitude between neighbouring bitstrings.

After a few rounds, the circuit is measured. Good schedules are not guaranteed, but the algorithm is trying to bias the measurement distribution toward low-cost bitstrings.

For the gate-level version of that idea, [Circuit Bench 07: QAOA for MaxCut](../../circuit-bench/07-qaoa-maxcut/README.md) is the side path. The staffing notebook uses the same phase-separator-and-mixer rhythm, but with a scheduling QUBO rather than a graph cut.

## The companion notebook

The notebook keeps the instance deliberately small: two nurses, two shifts, and a compact set of coverage and workload preferences.

That sounds almost absurdly small, but it lets every step stay visible:

- define the binary variables;
- build the QUBO penalties;
- convert the QUBO to an Ising form;
- check the exact classical costs for all assignments;
- run a one-layer QAOA circuit on Quokka;
- compare the measured bitstrings with the low-cost assignments.

In code, the structure is:

```python
Q = build_scheduling_qubo()
ising = qubo_to_ising(Q)
counts = run_qaoa(ising, gamma, beta)
```

The teaching point is the translation. A scheduling problem becomes a cost function; the cost function becomes an Ising Hamiltonian; the Hamiltonian becomes a circuit whose measurement samples candidate schedules.

The notebook is **not** a supply-chain optimiser. It does not solve a realistic rostering problem, tune penalty weights at scale, or compare against industrial mixed-integer solvers. It shows the smallest version of the modelling pipeline.

## Reality check

There are several places where this can fail before quantum hardware becomes the limiting factor.

First, the QUBO model has to be good. If the business objective is vague, if the constraints are missing, or if the penalty weights are badly chosen, the quantum circuit will faithfully optimise the wrong thing.

Second, the qubit count grows with the number of binary decisions. Real planning problems can require thousands or millions of variables before decomposition.

Third, QAOA is an optimisation heuristic. The choice of depth, angles, mixer, constraints, and post-processing all matter. A shallow circuit may be too weak; a deep circuit may be too noisy.

Quantum annealers, tensor-network methods, branch-and-bound solvers, local search, and classical decomposition all belong in the practical conversation. The notebook focuses on the gate-based QAOA route because it exposes the circuit mechanism directly.

The honest claim is this: QUBO and Ising formulations give a clean bridge from discrete planning to quantum optimisation circuits. The notebook shows that bridge in a four-bit scheduling toy. The real bottleneck is whether the model, hardware, and hybrid optimiser can scale together.

## Want more?

The [companion notebook](https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/06-supply-chains.ipynb) lets you build the scheduling QUBO, derive the Ising form, and run a one-layer QAOA instance. For the circuit pattern in isolation, see [Circuit Bench 07 — QAOA for MaxCut](../../circuit-bench/07-qaoa-maxcut/README.md).

---

*This is Unit 6 of The Quantum Bottleneck series. Next up: [The Materials Maze](bottleneck-07-materials-science.md) — when electrons in solids refuse to behave independently.*
