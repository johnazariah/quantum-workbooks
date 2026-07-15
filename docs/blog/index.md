---
hide:
  - toc
---

# Quantum computing, problem first

Most quantum computing explanations begin with a qubit. This blog usually does not.

We start with the problem, build the smallest runnable notebook that exposes the structure, and introduce the quantum machinery only when the problem asks for it. That does not mean skipping the foundations. It means earning them.

---

## Linear Algebra for Fun and Profit

The linear algebra behind quantum computing and machine learning. Each post builds from first principles with a single running example you can check by hand.

| | Post | One-line summary |
|---|---|---|
| Part 1 | [How to Raise *e* to a Matrix](posts/2026-07-14-how-to-raise-e-to-a-matrix.md) | The matrix exponential solves the Schrödinger equation, and the result is a rotation rather than a stretch. |
| Part 2 | [What a Difference *i* Makes](posts/2026-07-21-what-a-difference-i-makes.md) | Power iteration, imaginary time, and phase estimation are one move; the only difference is a factor of *i*. |

---

## The Quantum Bottleneck

Eight industry problems, each paired with the quantum algorithm that could solve it. Companion to the upcoming book. Every post follows the same rhythm: problem, bottleneck, quantum idea, notebook, reality check.

| Unit | Post | Problem domain | Algorithm |
|---|---|---|---|
| 1 | [The $50M Delivery Route](posts/bottleneck-01-logistics.md) | Logistics | QAOA / MaxCut |
| 2 | [The Trapdoor](posts/bottleneck-02-cryptography.md) | Cryptography | Shor / period-finding |
| 3 | [The $2B Molecule](posts/bottleneck-03-drug-discovery.md) | Drug discovery | VQE |
| 4 | [The Feature Explosion](posts/bottleneck-04-machine-learning.md) | Machine learning | Quantum kernels |
| 5 | [The Convergence Wall](posts/bottleneck-05-finance.md) | Finance | Amplitude estimation |
| 6 | [The Scheduling Nightmare](posts/bottleneck-06-supply-chains.md) | Supply chains | QUBO / Ising |
| 7 | [The Materials Maze](posts/bottleneck-07-materials-science.md) | Materials science | QPE / Hubbard |
| 8 | [The Catalyst Bottleneck](posts/bottleneck-08-climate-energy.md) | Climate / energy | VQE embedding |

Each post links to a [companion notebook](../bottleneck/index.md) you can run, and to the relevant [Circuit Bench](../circuit-bench/index.md) note for the gate-level machinery.

---

## From Saturday to Co-Author

A ten-part series documenting the journey from learning QAOA on a Saturday morning to co-authoring a quantum computing paper, eight weeks later. Written in Julia, grounded in functional programming, and published on the [main blog](https://johnazariah.github.io).

[Read the full series →](https://johnazariah.github.io/tags/from-saturday-to-coauthor/)

| | Post |
|---|---|
| 1 | [Saturday](https://johnazariah.github.io/2026/05/29/saturday-to-coauthor-01-saturday.html) |
| 2 | [The Fold Under the Tree](https://johnazariah.github.io/2026/06/01/saturday-to-coauthor-02-the-fold-under-the-tree.html) |
| 3 | [Three Gradients in One Codebase](https://johnazariah.github.io/2026/06/04/saturday-to-coauthor-03-three-gradients-in-one-codebase.html) |
| 4 | [The Walls](https://johnazariah.github.io/2026/06/08/saturday-to-coauthor-04-the-walls.html) |
| 5 | [The Algebra That Runs Itself](https://johnazariah.github.io/2026/06/11/saturday-to-coauthor-05-the-algebra-that-runs-itself.html) |
| 6 | [Eighteen Hundred Reasons](https://johnazariah.github.io/2026/06/15/saturday-to-coauthor-06-eighteen-hundred-reasons.html) |
| 7 | [Learning from the Masters](https://johnazariah.github.io/2026/06/18/saturday-to-coauthor-07-learning-from-the-masters.html) |
| 8 | [Fourteen](https://johnazariah.github.io/2026/06/22/saturday-to-coauthor-08-fourteen.html) |
| 9 | [The Collaborator That Never Sleeps](https://johnazariah.github.io/2026/06/25/saturday-to-coauthor-09-the-collaborator-that-never-sleeps.html) |
| 10 | [What Language Taught Us About Mathematics](https://johnazariah.github.io/2026/06/29/saturday-to-coauthor-10-what-language-taught-us-about-mathematics.html) |

---

## Where the pieces fit

- **The blog posts** (above) explain why a quantum idea appears and what it solves.
- **The [Companion Notebooks](../bottleneck/index.md)** let you run the idea.
- **The [Circuit Bench](../circuit-bench/index.md)** lets you slow down and inspect the circuit machinery.

Problem-first. Runnable. Honest.
