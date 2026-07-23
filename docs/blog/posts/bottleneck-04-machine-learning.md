---
date: 2026-08-08
notebook: https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/04-machine-learning.ipynb
categories:
- The Quantum Bottleneck
- Machine Learning
tags:
- quantum kernels
- SVM
- feature maps
- dequantisation
authors:
- John Azariah
social:
  linkedin: 'Machine learning works by moving data into a richer feature space. Quantum machine learning asks: what if the useful feature space is naturally quantum and classically awkward to compute? This post looks at quantum kernels, SVMs, and the dequantisation results that put a ceiling on the quantum speedup claims. The Netflix Prize is still a useful parable.


    #QuantumComputing #MachineLearning'
  bluesky: 'Bottleneck 04: The Feature Explosion. Quantum kernels promise richer feature spaces. Dequantisation results say: not so fast. This post walks through the honest gap.'
---

# The Feature Explosion

**Modern machine learning often works by moving data into a larger feature space. Quantum machine learning asks a sharper question: what if the useful feature space is naturally quantum, and classically awkward to compute?**

<!-- more -->

The Netflix Prize is still a useful parable. The problem was not just to recommend films. It was to infer preference from sparse, noisy, high-dimensional data: users, items, ratings, genres, histories, and all the interactions between them.

That is a familiar machine-learning move. When a problem is not linearly separable in the data we can see, we map it into a richer space where the separating surface may become simple. The cost is that richer spaces can become enormous.

Classical machine learning has a beautiful workaround: the **kernel trick**. Instead of explicitly constructing a feature vector $\phi(x)$, compute only the similarity

$$
K(x, x') = \langle \phi(x), \phi(x') \rangle .
$$

Support Vector Machines use those pairwise similarities to find a separating boundary. As long as $K(x, x')$ is cheap to evaluate, the feature space can be large without being explicitly stored.

The bottleneck appears when the similarity itself becomes the hard part.

## The bottleneck: kernels are only useful if you can compute them

It is tempting to say that high dimension is the problem. That is too blunt. High dimension is often the solution. The real problem is whether the geometry of that space can be accessed efficiently.

A kernel method needs a kernel matrix: every training point compared with every other training point. If there are $m$ training examples, that is $m^2$ kernel evaluations before the classifier even starts training.

So the practical question is not "can I imagine a useful feature space?" It is:

- can I encode the data into that space;
- can I compute the pairwise similarities;
- can I do both without smuggling in an even harder classical problem?

Quantum kernels live exactly at that boundary.

## The quantum idea: Hilbert space as feature space

A quantum feature map prepares a state $|\phi(x)\rangle$ from classical data $x$. The associated kernel is the overlap between two prepared states:

$$
K(x, x') = |\langle \phi(x') | \phi(x) \rangle|^2 .
$$

Operationally, this is a circuit experiment. Prepare $U_\phi(x)|0\rangle$, apply the inverse of $U_\phi(x')$, and measure the probability of returning to $|0\rangle$. If the circuit vocabulary is new, [Circuit Bench 00](../../circuit-bench/00-reading-a-quantum-circuit/README.md) explains gates, unitary rotations, and measurement before you meet them inside the kernel circuit.

The hybrid workflow is:

1. encode each data point with a quantum feature-map circuit;
2. estimate $K(x_i, x_j)$ from measurement counts;
3. assemble the kernel matrix;
4. train a classical SVM using that precomputed kernel.

The quantum computer is not replacing the whole classifier. It is being used as a kernel-estimation device.

## The companion notebook

The notebook builds a deliberately small quantum-kernel workflow:

- generate a two-dimensional half-moons dataset;
- encode each point into a two-qubit feature map using rotations and entanglement;
- estimate the kernel matrix by running overlap circuits;
- train a classical SVM on that quantum kernel;
- compare it with a classical RBF-kernel SVM.

The kernel circuit has the form:

```python
def kernel_circuit(x, xp):
    return U_phi(x) + U_phi_adjoint(xp) + measurement
```

The measured probability of `00` is the estimated overlap. Repeating that for every pair of training points gives the matrix passed to `SVC(kernel='precomputed')`.

This is a faithful worked example, not an advantage claim. With two features and a small synthetic dataset, a classical RBF kernel is already very strong. The point of the notebook is to make the quantum-kernel workflow concrete enough that the later caveats have somewhere to attach.

## Reality check

Quantum machine learning is one of the easiest areas to oversell, because the words line up too neatly: Hilbert spaces are large, machine learning likes large feature spaces, therefore quantum computers should help. The middle step is where the work is.

There are real theoretical separations. Some constructed classification tasks can be learned more efficiently with quantum kernels than by classical learners under the same access model. That matters, but it does not automatically translate into recommender systems, medical classifiers, or language models.

There are also real dequantisation results. Several proposed quantum machine-learning speedups became less compelling once classical algorithms were given comparable sampling or data-access assumptions. That does not kill quantum ML. It does make the target smaller and more precise.

The largest practical obstacle is often **data loading**. If a million classical features require a million gates to encode, the quantum feature map may lose before the kernel is ever measured. Quantum advantage is more plausible when the data is already quantum, when the feature map is compact, or when the classical simulation of the kernel circuit is genuinely hard.

So the honest claim is this: quantum kernels are a clean way to ask whether a quantum circuit can define a useful similarity measure. The notebook shows how that question becomes code. It does not show that today's quantum hardware improves practical machine learning.

## Want more?

The [companion notebook](https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/04-machine-learning.ipynb) lets you compare a two-qubit quantum kernel with a classical RBF kernel on the same toy dataset.

---

*This is Unit 4 of The Quantum Bottleneck series. Next up: [The Convergence Wall](bottleneck-05-finance.md) — when Monte Carlo is the only option and every extra digit of accuracy gets expensive.*
