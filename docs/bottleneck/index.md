# The Quantum Bottleneck — Companion Notebooks

**Eight industry problems. Eight quantum algorithms. Eight runnable notebooks.**

These are the companion notebooks for *The Quantum Bottleneck: Real Problems and their Quantum Solutions* — a book that teaches quantum computing application-first, starting from real industry problems rather than qubits.

Each notebook implements (or illustrates) the algorithm from its corresponding book chapter. Some are faithful worked examples; others are toy demonstrations where that is the honest way to show the idea at runnable scale.

!!! note "Pedagogy note"
    The code is intentionally explicit. We keep circuit construction, API calls, and measurement post-processing visible so you can inspect the mechanism end to end. A polished library would abstract more of this away — but that would make the teaching worse.

## The notebooks

| # | Unit | What you'll build | Blog post |
|---|------|-------------------|-----------|
| 1 | Logistics | QAOA variational loop for MaxCut on a small graph | [The $50M Delivery Route](../blog/posts/bottleneck-01-logistics.md) |
| 2 | Cryptography | Compiled period-finding toy for N = 15 | [The Trapdoor](../blog/posts/bottleneck-02-cryptography.md) |
| 3 | Drug Discovery | Single-geometry VQE anatomy for H₂ | [The $2B Molecule](../blog/posts/bottleneck-03-drug-discovery.md) |
| 4 | Machine Learning | Quantum vs. classical kernel SVM | [The Feature Explosion](../blog/posts/bottleneck-04-machine-learning.md) |
| 5 | Finance | Classical pricing + toy amplitude estimation | [The Convergence Wall](../blog/posts/bottleneck-05-finance.md) |
| 6 | Supply Chains | Nurse scheduling QUBO micro-example | [The Scheduling Nightmare](../blog/posts/bottleneck-06-supply-chains.md) |
| 7 | Materials Science | Hubbard benchmark and toy QPE | [The Unsimulable Material](../blog/posts/bottleneck-07-materials-science.md) |
| 8 | Climate & Energy | Embedding pipeline illustration for catalyst screening | [The Better Catalyst](../blog/posts/bottleneck-08-climate-energy.md) |

## Running locally

```bash
cd bottleneck
pip install -r requirements.txt
jupyter lab notebooks/
```

## About the book

*The Quantum Bottleneck* follows a zoom-in/zoom-out rhythm for each unit: **industry hook → mathematical bottleneck → quantum algorithm → worked example → reality check**. The full manuscript is being prepared for publication. These notebooks are the runnable companions — and the blog posts above are self-contained introductions to each problem.
