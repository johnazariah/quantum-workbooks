---
date: 2026-08-01
notebook: https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/02-cryptography.ipynb
categories:
- The Quantum Bottleneck
- Cryptography
tags:
- Shor's algorithm
- period-finding
- RSA
- QFT
- quantum phase estimation
authors:
- John Azariah
social:
  linkedin: 'The notebook factors 15. The problem is the cryptographic machinery that keeps the internet standing. Shor''s algorithm threatens RSA not by brute force but by turning factoring into period-finding, and period-finding into phase estimation. This post walks through the circuit, the quantum Fourier transform, and the honest gap between a toy demonstration and a real cryptographic threat.


    #QuantumComputing #Cryptography'
  bluesky: 'Bottleneck 02: The Trapdoor. The notebook factors 15. The problem is RSA. Shor''s algorithm turns factoring into period-finding, and the gap between 15 and a real key is the bottleneck.'
---

# The Trapdoor

The notebook factors 15.

The problem is the cryptographic machinery that keeps the internet standing.

That gap is the point.

<!-- more -->

RSA does not rely on secrecy about the method. The method is public. The modulus is public. The security rests on a one-way asymmetry:

```text
easy:  multiply two large primes
hard:  recover those primes from their product
```

If I hand you two large primes, multiplying them is routine. If I hand you only their product $N$, recovering the primes appears to be much harder. That asymmetry is the trapdoor. Knowing the factors lets you decrypt or sign. Not knowing them leaves you facing the factoring problem.

This is not a minor corner of computer science. RSA was published in 1978,[^rsa] and variants of the same public-key idea shaped the secure web, software updates, certificates, VPNs, messaging systems, and the everyday assumption that two machines can agree on secrets over a public network.

Classically, factoring is not known to be impossible. That matters. RSA is not protected by a proof that factoring is hard. It is protected by decades of evidence that the best known classical algorithms still do not make large RSA moduli easy to factor.

Then Shor found the crack.[^shor]

Not by trying possible factors faster.

By changing the problem.

## The shape under RSA

The notebook starts with $N = 15$ because 15 is the smallest RSA-shaped composite that lets the mechanism be visible without drowning us in arithmetic.

Of course nobody needs a quantum computer to factor 15.

That is not what the notebook is claiming.

The point is to expose the reduction that makes Shor's algorithm work. Pick a number $a$ that is coprime to $N$, and look at the function:

$$
f(x) = a^x \bmod N.
$$

For the notebook, $N = 15$ and $a = 7$.

Compute the first few values:

```text
x      0   1   2   3   4   5   6   7
7^x    1   7   4   13  1   7   4   13   (mod 15)
```

The values repeat every four steps. That repeating length is the **period**, or order, of $a$ modulo $N$:

$$
r = 4.
$$

If we know that period, the factors fall out by ordinary arithmetic. Since $r$ is even, compute:

$$
7^{r/2} = 7^2 \equiv 4 \pmod{15}.
$$

Then:

$$
\gcd(4 - 1, 15) = 3,
$$

and:

$$
\gcd(4 + 1, 15) = 5.
$$

So:

```text
15 = 3 x 5
```

The factoring problem has become a period-finding problem.

That is the first real move.

## Why period-finding is the bottleneck

The function $a^x \bmod N$ is easy to evaluate at any one $x$.

That does not mean the period is easy to find.

For large $N$, the period can be large, and the values can look irregular if you only sample them point by point. A classical machine can compute:

```text
f(0), f(1), f(2), ...
```

but finding the hidden repetition quickly is the hard part. Modern classical factoring algorithms are much more sophisticated than naive period search, but they still do not become polynomial-time factoring algorithms.

Shor's algorithm attacks the period directly. It arranges a quantum computation so that the period is written into phase, then uses a Fourier transform to make that phase measurable.

This is the second move:

```text
period in arithmetic -> phase in a quantum state -> measured bit string
```

If circuit words like gate, basis, or measurement are new, [Circuit Bench 00: Reading a Quantum Circuit](../../circuit-bench/00-reading-a-quantum-circuit/README.md) is the side path. You do not need it before reading this post, but it gives the basic vocabulary for the circuit operations below.

## The quantum move is phase estimation

The popular explanation of Shor's algorithm often says that a quantum computer tries all possible factors at once.

That is not the right picture.

Shor's algorithm does not search over factors. It estimates a period.

The clean way to say the quantum part is:

> Shor's algorithm uses quantum phase estimation on a modular-multiplication unitary.

That sentence is dense, so let us unpack only what the notebook needs.

Define a reversible operation:

$$
U_a |y\rangle = |ay \bmod N\rangle.
$$

This operation has eigenphases. Those phases contain fractions of the form:

$$
\frac{j}{r},
$$

where $r$ is the period we want.

Quantum Phase Estimation, or QPE, is the circuit pattern that estimates such a phase fraction. It uses a counting register, controlled powers of $U_a$, and an inverse Quantum Fourier Transform. For the gate-level version of that pattern, see [Circuit Bench 10: Quantum Phase Estimation](../../circuit-bench/10-quantum-phase-estimation/README.md).

The QFT is the piece that turns periodic phase structure into a measurement pattern. It is not a magic spectrum printer; by itself, a QFT output can look uniformly random when measured. Its power appears when it is used inside a larger interference pattern. [Circuit Bench 09: Quantum Fourier Transform](../../circuit-bench/09-quantum-fourier-transform/README.md) walks through that circuit directly.

The high-level Shor pipeline is:

```text
choose a
build modular multiplication by a mod N
run phase estimation
measure an approximation to j/r
use continued fractions to recover r
use gcd arithmetic to recover factors
```

The quantum computer does the period-finding step. The final extraction of factors is classical.

## What the notebook actually does

Open the notebook here:

[Unit 2 notebook: compiled period-finding for $N = 15$](https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/02-cryptography.ipynb)

The notebook is deliberately honest about its size.

It does **not** implement a scalable modular-exponentiation circuit. It does **not** claim to be a full Shor implementation for arbitrary $N$. It takes the $N = 15$, $a = 7$, $r = 4$ example and compiles one phase-estimation branch into a small circuit.

That choice is pedagogical, not evasive. Full modular arithmetic would hide the idea under a large amount of reversible bookkeeping. The workbook keeps the mechanism visible:

```text
classical reduction
compiled phase-estimation circuit
inverse QFT
continued fractions
gcd post-processing
```

### Section 1: Check the classical period

The notebook starts where it should: with the arithmetic.

```python
N = 15
a = 7
```

It computes the values of $7^x \bmod 15$ and verifies the repeating pattern:

```text
1, 7, 4, 13, 1, 7, 4, 13, ...
```

This gives the classical period $r = 4$.

That may seem like cheating, because we already know the answer.

For a teaching notebook, it is the right move. On a tiny instance, we should know the ground truth before asking whether the circuit output makes sense.

### Section 2: Compile one phase branch

For $r = 4$, the phase fractions are multiples of:

$$
\frac{1}{4}.
$$

The notebook chooses the branch:

$$
\frac{j}{r} = \frac{1}{4}.
$$

With three counting qubits, the phase-estimation register has:

$$
Q = 2^3 = 8
$$

possible values. The phase $1/4$ corresponds to:

$$
\frac{2}{8},
$$

so the expected measurement peak is the three-bit string:

```text
010
```

Instead of building the full modular-multiplication unitary, the notebook inserts the controlled phases for this branch directly:

```qasm
cu1(phase_angle) q[2], q[3];
cu1(2 * phase_angle) q[1], q[3];
cu1(4 * phase_angle) q[0], q[3];
```

This is the compiled toy. It demonstrates the QPE and inverse-QFT logic without pretending the hard arithmetic has been solved.

### Section 3: Measure the phase

The circuit runs many shots and counts the observed bit strings.

The important output is not a factor yet. It is a phase estimate. The dominant bit string should be:

```text
010
```

Interpreted as an integer, that is:

$$
k = 2.
$$

The phase estimate is:

$$
\frac{k}{Q} = \frac{2}{8} = \frac{1}{4}.
$$

Measurement gives a classical bit string. The number-theory work starts after that.

### Section 4: Recover the period

The notebook uses continued fractions:

```python
frac = Fraction(best_k, Q).limit_denominator(N)
r_candidate = frac.denominator
```

For the clean branch:

$$
\frac{2}{8} = \frac{1}{4},
$$

so the denominator is:

$$
r = 4.
$$

The notebook then checks:

$$
7^4 \equiv 1 \pmod{15}.
$$

That check matters. Real runs can produce unhelpful branches, noisy estimates, or candidate denominators that fail. Shor's algorithm is probabilistic: if a branch does not give a useful period, you try again.

### Section 5: Turn the period into factors

Once the period is recovered, the quantum work is over.

The notebook returns to classical arithmetic:

```python
x = pow(a, r // 2, N)
factor1 = math.gcd(x - 1, N)
factor2 = math.gcd(x + 1, N)
```

For $N = 15$, $a = 7$, and $r = 4$:

```text
x = 7^2 mod 15 = 4
gcd(4 - 1, 15) = 3
gcd(4 + 1, 15) = 5
```

That is the full toy pipeline.

Not "quantum magic factors 15."

Something more precise:

> A quantum phase-estimation circuit can expose a period, and classical number theory can turn that period into factors.

## What this shows, and what it does not

This notebook shows the skeleton of Shor's algorithm:

1. Factoring can be reduced to period-finding.
2. Period information can be encoded as quantum phase.
3. Phase estimation can turn that hidden phase into measured bits.
4. Continued fractions can recover the period from those bits.
5. GCD arithmetic can turn the period into factors.

That is the real architecture.

The notebook does not show the expensive part of a full implementation: reversible modular exponentiation at cryptographic scale. It also does not show error correction, fault-tolerant gates, magic-state factories, layout constraints, or any of the engineering needed to run Shor's algorithm against RSA-2048.

Those omissions are not small. They are the bottleneck between the theorem and the threat.

## Reality check

Shor's algorithm is mathematically settled. A large, fault-tolerant quantum computer would break RSA and related discrete-log cryptosystems.

The open question is not whether the algorithm works.

The open question is when the hardware exists.

Laboratory demonstrations of Shor-style factoring have stayed tiny, with examples such as 15 and 21.[^martin-lopez] Larger claims often use compiled circuits that bake in so much structure from the answer that they no longer represent scalable factoring.

For RSA-2048, the resource estimates are far beyond today's machines. Gidney and Ekera estimated that factoring a 2048-bit RSA integer in about eight hours would require roughly 20 million noisy physical qubits using surface-code error correction.[^gidney-ekera] Estimates will move as architectures improve, but the order of the challenge is the point: this is a fault-tolerant-era algorithm.

Cryptography is not waiting politely.

The reason is **harvest now, decrypt later**. An adversary can record encrypted traffic today and keep it until a future machine can decrypt it. That is why post-quantum cryptography is already moving from theory into standards and deployments. NIST released its first final post-quantum encryption and signature standards in 2024.[^nist-pqc]

So the practical message is balanced:

```text
not: quantum computers can break RSA today
not: RSA is safe forever
yes: Shor changes the long-term security assumption
yes: migration has to happen before the machine arrives
```

## What to try next

If you run the notebook, do not stop after seeing `15 = 3 x 5`.

Change the phase branch:

```python
target_j = 3
```

The fraction $3/4$ should still reveal denominator 4.

Then try:

```python
target_j = 2
```

That branch gives $1/2$, whose denominator is 2, not the full period. The notebook's validation step should catch that this candidate is not good enough for the factoring post-processing. This is a useful failure, because real Shor runs also have branches that force a retry.

Then inspect the `qpe_circuit` string itself. Trace the three controlled phase gates, then trace the inverse QFT. The useful lesson is not the number 15; it is the way phase gets converted into an ordinary bit string that continued fractions can use.

The larger story is not that factoring 15 is impressive. It is that the route from factoring to period-finding to phase estimation is visible end to end.

That route is why cryptographers took Shor seriously long before the hardware existed.

[^rsa]: Rivest, Shamir, and Adleman, ["A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"](https://people.csail.mit.edu/rivest/Rsapaper.pdf), Communications of the ACM, 1978.

[^shor]: Peter W. Shor, ["Algorithms for Quantum Computation: Discrete Logarithms and Factoring"](https://doi.org/10.1109/SFCS.1994.365700), 35th Annual Symposium on Foundations of Computer Science, 1994.

[^martin-lopez]: Martin-Lopez et al., ["Experimental realization of Shor's quantum factoring algorithm using qubit recycling"](https://doi.org/10.1038/nphoton.2012.259), Nature Photonics, 2012.

[^gidney-ekera]: Craig Gidney and Martin Ekera, ["How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits"](https://quantum-journal.org/papers/q-2021-04-15-433/), Quantum, 2021.

[^nist-pqc]: NIST, ["NIST Releases First 3 Finalized Post-Quantum Encryption Standards"](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards), 2024.

Next up: [The $2B Molecule](bottleneck-03-drug-discovery.md) — where the bottleneck is not a hidden period, but a quantum system too large to simulate directly.
