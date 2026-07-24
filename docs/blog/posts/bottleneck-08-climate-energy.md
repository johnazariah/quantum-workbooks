---
date: 2026-08-22
notebook: https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/08-climate-energy.ipynb
categories:
- The Quantum Bottleneck
- Climate & Energy
tags:
- quantum embedding
- VQE
- catalysis
- active spaces
- climate tech
authors:
- John Azariah
social:
  linkedin: 'The energy transition needs better catalysts for water splitting, CO2 reduction, nitrogen fixation, and battery chemistry. Catalyst design is an electronic-structure problem in disguise. This final post in The Quantum Bottleneck runs a VQE calculation on a small active space and closes the series with an honest assessment: quantum computing is not a shortcut past chemistry, but it may be the only path through certain problems classical computers cannot reach.


    #QuantumComputing #ClimateTech'
  bluesky: 'Bottleneck 08: The Catalyst Bottleneck. Climate tech needs better catalysts. Catalyst design is electronic structure in disguise. The series closer asks honestly: where does quantum computing fit?'
---

# The Catalyst Bottleneck

**Climate technology is full of chemistry problems. Better catalysts could change the cost of clean fuels, fertiliser, carbon utilisation, and industrial heat, but catalyst design is an electronic-structure problem in disguise.**

<!-- more -->

The energy transition is not only about deploying known technologies. It is also about finding materials that make difficult reactions cheap, selective, and durable.

Split water. Reduce carbon dioxide. Fix nitrogen. Store energy in chemical bonds. Move ions through a battery. In each case, the practical question is not just "does the reaction happen?" It is "does it happen fast enough, selectively enough, and at a cost we can tolerate?"

Catalysts answer those questions through electronic structure. The active site has to bind intermediates neither too weakly nor too strongly, move charge at the right time, and survive the operating environment. That is precisely the regime where classical modelling can become uncertain.

## The bottleneck: the active site is not the whole system

A catalyst is not an isolated molecule floating in a vacuum. The chemically important active site sits inside an environment: a surface, a support, a solvent, an electrolyte, a protein scaffold, or a larger material.

Classical methods handle much of that environment well. The difficulty is the strongly correlated fragment where bond breaking, charge transfer, spin state changes, or transition-metal orbitals dominate the answer.

A brute-force quantum calculation of the whole system is impossible. A tiny active-site calculation without the environment is often too crude.

That is the embedding problem: keep the large environment classical enough to be tractable, but solve the hard active space accurately enough that the chemistry is meaningful.

## The quantum idea: embed first, solve the hard fragment

Quantum embedding turns the workflow into pieces:

1. use classical computation to choose an active space;
2. compress the environment into an effective Hamiltonian for that active space;
3. solve the active-space Hamiltonian with a stronger quantum or classical method;
4. feed the result back into the larger calculation if the embedding scheme requires self-consistency.

The quantum computer is not asked to solve the whole catalyst. It is asked to solve the part where the electronic structure is hardest.

In a near-term teaching setting, that solve step is naturally illustrated with VQE: prepare a parameterised state, measure Pauli terms, combine the measurements into an energy, and let a classical loop search over the parameter. [Circuit Bench 08: VQE for H2](../../circuit-bench/08-vqe-h2/README.md) shows that measurement pattern in its smallest chemistry form.

## The companion notebook

The notebook is a pipeline illustration, not a catalyst simulation package.

It starts after the classical embedding work has already happened. The active-space Hamiltonian is precomputed as a two-qubit toy model with Pauli terms such as $Z_0$, $Z_1$, $Z_0Z_1$, $X_0X_1$, and $Y_0Y_1$.

Then the notebook executes one embedded solve step:

- compare a classical embedding baseline with an exact benchmark for the reduced model;
- prepare a one-parameter entangling ansatz;
- measure the Pauli terms in the required bases;
- combine the measurements into an energy estimate;
- compare the VQE result with the exact embedded benchmark.

In code, the shape is:

```python
coeffs = embedded_active_space_coeffs()
E_exact = exact_diagonalisation_energy(coeffs)
E_vqe = compute_active_energy(theta, coeffs, shots=1024)
```

The important absences are just as important as the code:

- the notebook does not run DFT;
- it does not construct a DMET bath;
- it does not choose the active space dynamically;
- it does not run a self-consistent embedding loop;
- it does not compute a real catalyst binding trend.

It shows where the quantum subroutine would sit once those surrounding classical pieces have supplied the reduced Hamiltonian.

## Reality check

Embedding is attractive because it gives quantum hardware a focused job. That is also what makes it difficult. The interface between the classical environment and the quantum active space has to be accurate, stable, and scientifically interpretable.

The active space must include the orbitals that actually drive the chemistry. The effective Hamiltonian must preserve the relevant environmental effects. The quantum solver must reach chemical accuracy for the reduced problem. The final workflow must turn energy differences into useful catalyst trends rather than isolated numbers.

And the hardware still matters. VQE-style solve steps face measurement cost, optimiser noise, ansatz limitations, and device errors. Phase-estimation-style solve steps are cleaner in principle but need fault tolerance.

So the honest claim is not that quantum computers will "solve climate." The claim is more precise: some climate and energy technologies depend on hard electronic-structure calculations, and embedding is one plausible way to place a quantum solver exactly where that hardness lives.

The notebook shows that placement in miniature.

## Want more?

The [companion notebook](https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/08-climate-energy.ipynb) lets you run the precomputed embedded active-space VQE solve step. For the circuit-level VQE measurement pattern, see [Circuit Bench 08 — VQE for H2](../../circuit-bench/08-vqe-h2/README.md).

---

*This is Unit 8 of The Quantum Bottleneck series. Return to the [series overview](../../bottleneck/index.md) for the full companion path.*
