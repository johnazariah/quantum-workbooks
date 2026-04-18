# References

Curated recommendations for going deeper. These are the resources we actually use and recommend — not an exhaustive bibliography.

---

## Textbooks

### Introductory

| Book | Authors | Why we recommend it |
|------|---------|---------------------|
| *Quantum Computing: An Applied Approach* (2nd ed.) | Jack Hidary | Practical, code-forward, covers real algorithms with implementations |
| *Quantum Computation and Quantum Information* | Nielsen & Chuang | The classic. Dense but definitive. Best used as a reference after you have intuition |
| *An Introduction to Quantum Computing* | Kaye, Laflamme, Mosca | Cleaner than N&C for a first pass; good balance of theory and algorithms |
| *Quantum Computer Science* | Mermin | Wonderfully clear writing. Best "second book" for CS people |

### For physicists and chemists

| Book | Authors | Why we recommend it |
|------|---------|---------------------|
| *Quantum Chemistry in the Age of Quantum Computing* | Babbush et al. | The bridge between chemistry and quantum algorithms |
| *Modern Quantum Chemistry* | Szabo & Ostlund | Classical comp-chem foundations; essential if you want to understand VQE deeply |
| *Qubit-Efficient Encodings for Binary Optimisation Problems* | Azariah et al. | Shameless plug — our book on encoding fermions onto qubits. Companion to this cookbook for quantum simulation recipes |

### For the mathematically inclined

| Book | Authors | Why we recommend it |
|------|---------|---------------------|
| *Quantum Information Theory* | Mark Wilde | Rigorous information-theoretic foundations |
| *Quantum Computing Since Democritus* | Scott Aaronson | Half philosophy, half complexity theory, entirely entertaining |

---

## Online courses

| Course | Platform | Level |
|--------|----------|-------|
| [Quantum Computing for Everyone](https://www.edx.org/learn/quantum-computing) | edX (Chris Bernhardt) | Beginner — no linear algebra required |
| [Introduction to Quantum Computing](https://www.coursera.org/learn/quantum-computing-algorithms) | Coursera (various) | Undergrad — assumes basic linear algebra |
| [Qiskit Textbook](https://learning.quantum.ibm.com/) | IBM Quantum | Self-paced — interactive, excellent visualizations |
| [Quantum Computation (Preskill)](http://theory.caltech.edu/~preskill/ph229/) | Caltech | Graduate — the gold standard lecture notes |

---

## Key papers

These are the papers behind the recipes. Each recipe references the relevant paper directly; this is the collected list.

| Paper | Year | Relevant recipe |
|-------|------|-----------------|
| Einstein, Podolsky, Rosen — "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" | 1935 | Bell State |
| Bell — "On the Einstein Podolsky Rosen Paradox" | 1964 | Bell State |
| Bennett et al. — "Teleporting an Unknown Quantum State" | 1993 | Teleportation |
| Deutsch & Jozsa — "Rapid Solution of Problems by Quantum Computation" | 1992 | Deutsch-Jozsa |
| Grover — "A Fast Quantum Mechanical Algorithm for Database Search" | 1996 | Grover's Search |
| Farhi, Goldstone, Gutmann — "A Quantum Approximate Optimization Algorithm" | 2014 | QAOA |
| Peruzzo et al. — "A Variational Eigenvalue Solver on a Photonic Quantum Processor" | 2014 | VQE |
| Shor — "Algorithms for Quantum Computation" | 1994 | QPE / QFT |

---

## Community and tools

| Resource | What it is |
|----------|------------|
| [Quokka](https://www.quokkacomputing.com/) | The 30-qubit quantum computing platform these recipes are built for |
| [OpenQASM 2.0 spec](https://openqasm.com/) | The language every recipe is written in |
| [Qiskit](https://qiskit.org/) | IBM's full-stack quantum SDK — if you want to go beyond QASM |
| [Quirk](https://algassert.com/quirk) | Drag-and-drop quantum circuit simulator in the browser — great for visual intuition |
| [Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com/) | The best Q&A site for quantum computing questions |

---

## Notation guide

We use standard Dirac notation throughout the cookbook:

| Symbol | Meaning |
|--------|---------|
| $\|0\rangle$, $\|1\rangle$ | Computational basis states |
| $\|+\rangle$, $\|-\rangle$ | Superposition states $\frac{1}{\sqrt{2}}(\|0\rangle \pm \|1\rangle)$ |
| $H$ | Hadamard gate |
| $\text{CNOT}$, $CX$ | Controlled-NOT gate |
| $\otimes$ | Tensor product (combining systems) |
| $\langle \psi \| \phi \rangle$ | Inner product / overlap |

If the notation in a recipe ever feels unfamiliar, check back here or follow the links in the recipe's "Ingredients" section.
