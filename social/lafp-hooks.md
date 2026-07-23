# Linear Algebra for Fun and Profit — Social Hooks

## Part 1: How to Raise `e` to a Matrix (Jul 14)

### LinkedIn
How do you raise e to a matrix, and why would you want to? The matrix exponential solves the Schrödinger equation, powers quantum time evolution, and hides a geometric insight: when the matrix is Hermitian, the result is a rotation of state space. This post builds the whole story from scratch with one running example, a 2×2 matrix you can check by hand. The spectral theorem, projectors, phase geometry, and interference, all from first principles.

#LinearAlgebra #QuantumComputing

### Bluesky
New series: Linear Algebra for Fun and Profit. Part 1 builds the matrix exponential from scratch and shows why e^{-iHt} is a rotation. One running example, first principles, no prerequisites beyond linear algebra.

---

## Part 2: Where Eigenvalues Pay Rent (Jul 17)

### LinkedIn
Last week I showed how to raise e to a matrix. This week: where that machinery earns its keep. Google's PageRank is the dominant eigenvector of the web's link matrix, found by the simplest eigensolver in existence. Portfolio risk management decomposes a covariance matrix to hedge 500 stocks with 10 trades. Molecular simulation seeks the ground-state eigenvalue of a Hamiltonian that grows exponentially with molecule size. Three industries, three matrices, same spectral theorem. The tools come in Parts 3 and 4.

#LinearAlgebra #MachineLearning

### Bluesky
Part 2 is up. PageRank, portfolio risk, molecular simulation: three industries, three matrices, same spectral theorem. The tools come next.

---

## Part 3: The Eigensolver Zoo (Jul 21)

### LinkedIn
Part 2 showed where eigenvalues pay rent. Part 3 shows how you compute them. Power iteration applies the matrix repeatedly and lets the dominant eigenvector win. Lanczos builds a small subspace and extracts the extremes in a handful of matrix-vector products. Imaginary time replaces the i in the propagator with a real exponent and lets the ground state float to the top. Every classical eigensolver is a function of the operator applied to stretch the spectrum. Part 4 drops Thursday, where stretch becomes rotation and a single factor of i separates classical from quantum.

#LinearAlgebra #QuantumComputing

### Bluesky
Part 3: the classical eigensolver zoo. Power iteration, Lanczos, imaginary time. Every one stretches the spectrum to amplify an extremal eigenvector. Part 4 crosses to quantum, where stretch becomes rotation.

---

## Part 4: What a Difference `i` Makes (Jul 24)

### LinkedIn
The classical eigensolvers in Part 3 all stretch: they apply functions of the operator with real exponents to amplify an extremal eigenvector. Insert a single factor of i and stretching becomes rotation. Eigenvalues move onto the unit circle, lengths are preserved, and a quantum computer can run the evolution natively. That is the entire content of quantum phase estimation, the variational quantum eigensolver, and adiabatic state preparation. Four posts, one idea: the spectral theorem is the load-bearing structure under web search, portfolio risk, molecular simulation, and every eigensolver classical or quantum. The difference between the classical half and the quantum half is one letter.

#QuantumComputing #LinearAlgebra

### Bluesky
Part 4 closes the series. Insert i into the exponent and stretch becomes rotation. QPE, VQE, adiabatic prep: all one move. Same spectral theorem, one letter apart.
