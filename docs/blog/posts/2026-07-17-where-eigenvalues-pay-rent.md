---
date: 2026-07-17
categories:
  - Linear Algebra for Fun and Profit
tags:
  - eigenvalues
  - machine learning
  - applications
authors:
  - John Azariah
social:
  linkedin: |
    Last week I showed how to raise e to a matrix. This week: where that machinery earns its keep. Google's PageRank is the dominant eigenvector of the web's link matrix, found by the simplest eigensolver in existence. Portfolio risk management decomposes a covariance matrix to hedge 500 stocks with 10 trades. Molecular simulation seeks the ground-state eigenvalue of a Hamiltonian that grows exponentially with molecule size. Three industries, three matrices, same spectral theorem. The tools come in Parts 3 and 4.

    #LinearAlgebra #MachineLearning
  bluesky: "Part 2 is up. PageRank, portfolio risk, molecular simulation: three industries, three matrices, same spectral theorem. The tools come next."
---

# Where Eigenvalues Pay Rent

*Part 1 built the spectral theorem. Before we survey the tools that compute eigenvalues, here is why you would want to: three industries, three matrices, three ways the same decomposition does real work.*

<!-- more -->

!!! note "Part 2 of *Linear Algebra for Fun and Profit*"
    Part 1, **How to Raise `e` to a Matrix**, builds the machinery this post spends: the spectral theorem, the matrix exponential, and why $e^{-iHt}$ is a rotation. This post shows where that machinery lands; Parts 3 and 4 survey the classical and quantum tools that compute the eigenvalues.

!!! quote "Dedication"

    For Dave Probert, whose humour and friendship have been valuable to me since our time at QuArC, and who continues to mentor, inspire and refine my views on work, life and computing.

## Three matrices, one theorem

Every application in this post reduces to the same question: *what are the eigenvalues and eigenvectors of a particular matrix?* The matrix changes — a link graph, a covariance table, a molecular Hamiltonian. The scale changes — millions of web pages, thousands of stocks, dozens of electrons. The tool changes — power iteration, the singular value decomposition (SVD), and the variational quantum eigensolver (VQE). But the spectral theorem is always the engine, and the eigenvectors are always the answer.

---

## 1. Ranking the web

In 1998, the web had roughly 150 million pages. A user types a query and gets thousands of matches. Which ones matter?

Larry Page and Sergey Brin's insight[^pagerank1999] was to define importance recursively: a page is important if important pages link to it. That circular definition is an eigenvector equation.

Let $A$ be the web's link matrix: $A_{ij} = 1/d_j$ if page $j$ links to page $i$ (where $d_j$ is the number of outgoing links from $j$), and zero otherwise. Each column sums to 1, so $A$ is a column-stochastic matrix. The importance scores $\mathbf{x}$ satisfy

$$A\mathbf{x} = \mathbf{x},$$

the dominant eigenvector of $A$, guaranteed positive by the Perron-Frobenius theorem (after adding a damping factor to handle dead ends and cycles).

The tool is power iteration — the simplest eigensolver in existence. Start with uniform scores, repeatedly compute $\mathbf{x} \leftarrow A\mathbf{x}$, normalise, and wait for convergence. On the early web this took about 50 iterations over the full link graph, a matter of hours on a cluster. The result is a single vector of scores, precomputed once and looked up at query time.

PageRank was the algorithmic foundation of Google Search. The company was valued at \$23B at its 2004 IPO and reached \$1T in 2020. The dominant eigenvector of a sparse matrix, found by the oldest trick in linear algebra, underpinned a substantial fraction of that value.

Modern search ranking uses hundreds of signals beyond PageRank — click data, language models, freshness, authority scores — and PageRank alone has not been sufficient for years. But the structural insight, that network importance is an eigenvector, remains the foundation, and the same computation appears in social network analysis, citation ranking, and any setting where influence flows through a graph. Part 3 covers power iteration in detail and shows the same three lines of code ranking nodes on a small network.

---

## 2. Hedging 500 stocks with 10 trades

A portfolio manager holds positions in 500 stocks. Each stock moves daily, and the movements are correlated: tech stocks tend to move together, oil companies respond to the same commodity price, banks share interest-rate exposure. The manager needs to understand and control the portfolio's total risk, but 500 correlated variables are too many to reason about directly.

The matrix this time is the $500 \times 500$ covariance matrix $\Sigma$, where $\Sigma_{ij}$ is the covariance of stock $i$'s returns with stock $j$'s. This matrix is symmetric and positive semi-definite — it is Hermitian with non-negative eigenvalues — so the spectral theorem applies directly:

$$\Sigma = \sum_{k=1}^{500} \lambda_k \, \mathbf{v}_k \, \mathbf{v}_k^\top.$$

Each eigenvector $\mathbf{v}_k$ is a *principal component*: a linear combination of stocks that moves independently of all the others. The eigenvalue $\lambda_k$ is the variance explained by that component — how much of the portfolio's total risk lives along that direction.

In practice, a handful of eigenvalues dominate. The largest eigenvector is typically the "market factor" (everything goes up or down together). The next few capture sector rotations (tech vs. energy, growth vs. value). The remaining hundreds are noise: small eigenvalues, idiosyncratic stock-level jitter.

This is Principal Component Analysis[^jolliffe2002], and it is the backbone of quantitative risk management. A risk manager who knows the top 10 eigenvectors of the covariance matrix can hedge 80–90% of the portfolio's variance with 10 trades instead of 500. The Barra risk model, used by most institutional investors, is essentially a curated spectral decomposition of the equity covariance matrix, updated daily. The same decomposition drives recommender systems (Netflix, Spotify), dimensionality reduction in genomics, image compression (the eigenfaces of face recognition), and latent semantic analysis in NLP. In each case, the eigenvectors of a symmetric matrix reveal the axes along which the data actually varies, as opposed to the axes you happened to measure.

One thing to be careful about: covariance matrices estimated from finite data are noisy, and the eigenvectors of a noisy matrix are not the eigenvectors of the true matrix — particularly the small-eigenvalue ones. Random matrix theory (the Marcenko-Pastur distribution) tells you which eigenvalues are signal and which are sampling noise[^laloux2000]. A risk model that trusts all 500 eigenvectors equally is overfitting the past; a good one discards or shrinks the noisy components. The spectral theorem gives the decomposition; knowing which eigenvalues to believe requires statistics.

---

## 3. The ground state is worth billions

A pharmaceutical company wants to know whether a candidate drug molecule will bind to a protein target. The binding energy depends on the molecule's electronic ground-state energy — the lowest eigenvalue of the molecular Hamiltonian. Classical quantum chemistry computes this routinely for small molecules (up to about 50 electrons with current methods), but the Hilbert space grows exponentially: a molecule with $N$ spin-orbitals has a $2^N$-dimensional Hamiltonian, and beyond $N \approx 50$ even Lanczos on a supercomputer cannot store the state vector.

The electronic Hamiltonian $H$ in second quantisation, after choosing a basis of spin-orbitals, is a sum of one-body and two-body terms:

$$H = \sum_{pq} h_{pq} \, a_p^\dagger a_q + \frac{1}{2} \sum_{pqrs} h_{pqrs} \, a_p^\dagger a_q^\dagger a_r a_s.$$

Mapped to qubits (via Jordan-Wigner or Bravyi-Kitaev encoding), this becomes a sum of Pauli strings. The ground-state energy $E_0$ is the smallest eigenvalue. It is a real number because $H$ is Hermitian — that is the spectral theorem doing its work: real eigenvalues, orthogonal eigenstates, and the variational principle that says any trial state gives an upper bound.

On a classical computer the options are: full configuration interaction (exact diagonalisation, exponential cost), coupled cluster (approximate, polynomial cost, gold standard for weakly correlated systems), and density functional theory (mean-field, fast, less accurate for strongly correlated systems). These are all eigensolvers or approximations to eigensolvers, and they all hit the memory wall at some molecule size. On a quantum computer: VQE for near-term devices or QPE (quantum phase estimation) for fault-tolerant ones. Parts 3 and 4 survey both sides in detail.

The global pharmaceutical market spends roughly \$250B per year on R&D[^pharma2024]. If quantum eigensolvers can handle strongly correlated molecules that classical methods cannot — transition-metal catalysts, metalloenzymes, excited states in photovoltaics — the value is not in replacing classical chemistry but in reaching systems that are currently intractable. The same Hamiltonian eigenproblem governs materials science (band structures, superconductors), catalysis (nitrogen fixation, CO$_2$ reduction), and nuclear physics (shell-model Hamiltonians). In each case the ground-state energy is the quantity of interest, and the Hilbert-space dimension is the wall.

That said: no quantum computer has yet computed a molecular energy that a classical computer could not compute more accurately and more cheaply. The smallest demonstrations — H$_2$, LiH, BeH$_2$ — are well within classical reach. The crossover point is an open research question, with estimates ranging from 100 to 1000 logical qubits with error correction. The spectral theorem guarantees the answer exists; whether quantum hardware can reach it before classical algorithms improve further is the race.

---

## The ledger

| application | matrix | eigenvector is | eigenvalue is | tool | what it bought |
|---|---|---|---|---|---|
| web search | link matrix $A$ | importance scores | 1 (stochastic) | power iteration | \$100B+ company |
| risk management | covariance $\Sigma$ | hidden risk factor | variance explained | SVD / PCA | hedge 500 stocks with 10 trades |
| molecular simulation | Hamiltonian $H$ | ground state $\lvert E_0\rangle$ | binding energy $E_0$ | VQE / QPE | reach intractable molecules |

Three different matrices, three different industries, three different scales. The spectral theorem is the same in every row. The eigenvalues are always real because the matrices are always Hermitian (or symmetric, the real case). The eigenvectors always form an orthonormal basis that reveals hidden structure — importance, risk factors, quantum states.

## What comes next

Two of these three applications live on the stretch side of the $i$-factor divide: PageRank uses real power iteration ($H^k$), and PCA uses the real spectral decomposition of a symmetric matrix. Neither involves complex numbers or unitary evolution. The third, molecular ground-state energy, uses both sides: classical methods apply the stretch (imaginary time, Lanczos), while quantum methods apply the rotation ($e^{-iHt}$ for QPE) or minimise the Rayleigh quotient over unitary circuits (VQE).

Part 3 surveys the classical tools — the stretch — and Part 4 crosses to the quantum side, where the only difference is a single factor of $i$.

[^pagerank1999]: L. Page, S. Brin, R. Motwani, and T. Winograd, "The PageRank Citation Ranking: Bringing Order to the Web," Stanford InfoLab Technical Report (1999).
[^jolliffe2002]: I. T. Jolliffe, *Principal Component Analysis*, 2nd ed., Springer (2002).
[^laloux2000]: L. Laloux, P. Ciqui, J.-P. Bouchaud, and M. Potters, "Random Matrix Theory and Financial Correlations," *Int. J. Theor. Appl. Finance* **3**(3), 391–397 (2000).
[^pharma2024]: IQVIA Institute, *Global Trends in R&D*, 2024.
