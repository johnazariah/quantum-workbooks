---
date: 2026-08-05
notebook: https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/03-drug-discovery.ipynb
categories:
- The Quantum Bottleneck
- Drug Discovery
tags:
- VQE
- molecular simulation
- quantum chemistry
- electronic structure
authors:
- John Azariah
social:
  linkedin: 'Getting a drug to market costs roughly $2B, and a substantial fraction goes to molecular screening. Before a molecule reaches a clinical trial, we often do not know enough about how its electrons behave. VQE promises to compute electronic structure on a quantum computer, but the gap between a hydrogen molecule on a simulator and a real drug candidate is vast. This post walks through both sides honestly.


    #QuantumComputing #DrugDiscovery'
  bluesky: 'Bottleneck 03: The $2B Molecule. VQE computes electronic structure for drug candidates, but the gap between a hydrogen molecule on a simulator and a real drug is the bottleneck.'
---

# The $2B Molecule

**Drug discovery is expensive because biology is not the only uncertainty. Before a molecule ever reaches a clinical trial, we often do not know enough about how its electrons behave.**

<!-- more -->

A candidate drug is not just a shape in a docking diagram. It is a quantum system: nuclei, electrons, charges, orbitals, and bonds. Whether it binds to a target, whether it prefers one conformation over another, and whether it participates in the chemistry we want are all consequences of electronic structure.

That is the promise behind computational chemistry in drug discovery. If we could predict the relevant molecular energies accurately enough, early screening would become less empirical. Fewer dead ends would be synthesised. Fewer candidates would enter expensive experiments for the wrong reasons.

The catch is that the calculation we want is the one classical computers struggle to do exactly.

## The bottleneck: electron correlation

Electrons are not little planets orbiting nuclei independently. They are indistinguishable quantum particles whose joint state must obey antisymmetry, Coulomb repulsion, and the Pauli principle. The difficult part is **correlation**: the way the motion of one electron changes the possible motion of the others.

Classical chemistry therefore lives on a ladder of approximations:

- **Hartree-Fock** gives each electron an average field from the others. It is fast, but it misses much of the correlation energy.
- **Density functional theory** replaces the full wavefunction with electron density. It is often very useful, but accuracy depends on the functional and can fail for strongly correlated systems.
- **Coupled-cluster and configuration-interaction methods** recover more correlation, but the cost rises steeply.
- **Full configuration interaction** is exact within a chosen basis, but the state space grows exponentially.

That exponential growth is not rhetorical. If $N$ electrons can occupy $M$ spin-orbitals, the number of allowed configurations grows like $\binom{M}{N}$. The active spaces that matter for catalysis, transition metals, and bond breaking can become too large for exact classical treatment.

## The quantum idea: estimate the energy directly

A quantum computer does not make chemistry easy. What it changes is the representation problem. Qubits can store and manipulate quantum amplitudes without writing the full state vector into classical memory.

For chemistry, the usual workflow is:

1. choose a molecular geometry and basis;
2. build a fermionic Hamiltonian for the electrons;
3. encode that Hamiltonian as qubit operators;
4. prepare a trial quantum state;
5. measure the expected energy;
6. let a classical optimiser adjust the circuit and try again.

That loop is the **Variational Quantum Eigensolver**, or VQE. The principle underneath it is simple: for any trial state $|\psi(\theta)\rangle$,

$$
\langle \psi(\theta) | H | \psi(\theta) \rangle \geq E_0,
$$

where $E_0$ is the true ground-state energy of the Hamiltonian. Lower trial energy means a better approximation to the ground state.

The quantum computer prepares and measures $|\psi(\theta)\rangle$. The classical computer chooses the next $\theta$. The algorithm is hybrid because neither side is doing the whole job.

If the measurement-basis language feels sudden, [Circuit Bench 00](../../circuit-bench/00-reading-a-quantum-circuit/README.md) gives the one-qubit version first. For the chemistry-specific circuit used here, [Circuit Bench 08](../../circuit-bench/08-vqe-h2/README.md) walks through the H2 VQE measurement circuit.

## The companion notebook

The notebook deliberately does **not** pretend to be a drug-discovery platform. It works with the smallest useful chemistry example: a reduced two-qubit Hamiltonian for $\mathrm{H}_2$ at one bond length.

That scope matters. The notebook does not build molecular integrals from scratch, does not scan a full potential-energy surface, and does not model a protein binding pocket. It shows the anatomy of the VQE loop:

- a precomputed reduced $\mathrm{H}_2$ Hamiltonian;
- an exact diagonalisation benchmark for that same reduced model;
- a Hartree-Fock reference state;
- a one-parameter ansatz circuit;
- direct measurements in the $Z$, $X$, and $Y$ bases for the Pauli terms;
- a parameter sweep that compares the VQE estimate with the exact benchmark.

In code, the shape is:

```python
coeffs = h2_hamiltonian_coeffs()
E_exact = exact_diagonalisation_energy(coeffs)

for theta in thetas:
    energy = compute_energy(theta, coeffs, shots=1024)
```

The teaching point is not that two qubits are chemically impressive. They are not. The point is that the full VQE pattern is visible: encode a Hamiltonian, prepare a trial state, measure Pauli expectations, combine them into an energy, and use a classical loop to search for a lower value.

## Reality check

VQE became attractive because it uses shallower circuits than phase-estimation-based chemistry. That makes it a natural algorithm to test on noisy hardware. But "shallower" is not the same as "easy."

There are three hard problems hiding behind the small H2 example.

First, the **measurement cost** grows. A realistic molecular Hamiltonian can contain many Pauli terms, and each term needs enough shots to estimate its contribution accurately. Grouping commuting terms, classical shadows, and other measurement strategies help, but they do not remove the issue.

Second, the **ansatz matters**. A circuit that cannot represent the relevant chemistry will not find the right energy, no matter how clever the optimiser is. A very expressive circuit may become too deep or too hard to optimise.

Third, **scale changes the story**. A drug-sized system is not two qubits at one bond length. The credible path is an active-space calculation: use classical methods for the parts they handle well, and reserve the quantum device for the strongly correlated subproblem.

So the honest claim is narrow but important: VQE is a concrete way to turn molecular energy estimation into a quantum-classical loop. The notebook shows that loop in its smallest form. The bottleneck is what happens when the active space stops being small.

## Want more?

The [companion notebook](https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/03-drug-discovery.ipynb) lets you run the single-geometry $\mathrm{H}_2$ VQE anatomy demo. For the gate-level side path, see [Circuit Bench 08 — VQE for H2](../../circuit-bench/08-vqe-h2/README.md).

---

*This is Unit 3 of The Quantum Bottleneck series. Next up: [The Feature Explosion](bottleneck-04-machine-learning.md) — when the data bottleneck moves from molecules to feature spaces.*
