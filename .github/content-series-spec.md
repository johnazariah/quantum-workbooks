# Content Series Specification

Design document for the quantum blog's content pipeline. Each series below is
derived from research learnings already written up in the PhD workspace. An agent
assigned to a series should: (1) read the source material, (2) propose a coherent
post sequence with titles and one-paragraph abstracts, (3) draft each post in the
blog's voice, (4) refine and polish, (5) generate social hooks per the social-hook
skill.

Written: 2026-07-16. Authoritative location: `.github/content-series-spec.md` in
the `johnazariah/quantum` repository.

---

## Principles

- **One idea per post.** Each post should have a single organising insight the reader
  takes away. If you find yourself writing "but that is another story," you have found
  the next post.
- **Build on the previous.** Posts in a series form a dependency chain: each post may
  assume the reader has read the preceding ones but nothing else.
- **Concrete before abstract.** Lead with a worked example, a picture, or a
  motivating application. The general theory follows.
- **Voice.** Technical but accessible. No jargon without immediate explanation. No
  emoji. No clickbait. Matter-of-fact register. Humour is welcome but must earn its
  place.
- **Format.** MkDocs Material blog post. Use admonitions for asides, MathJax for
  equations, Mermaid for diagrams where helpful. Code samples in Python or Julia with
  syntax highlighting.
- **Length.** Target 2000–4000 words (10–20 min read). Longer is acceptable if the
  idea genuinely requires it, but split if possible.
- **Social hooks.** Each post gets a LinkedIn hook (~150 words, broad audience, lead
  with applications) and a Bluesky blurb (≤300 chars, technical audience). See
  `.github/skills/social-hook/SKILL.md` for voice constraints.

---

## Series 1: QAOA from Scratch

**Source material:** `qaoa-xorsat/.project/learning/` (35+ files)

**Thesis:** QAOA is quantum interference applied to combinatorial optimisation. This
series builds it from zero, arrives at the Walsh-Hadamard factorisation (our original
contribution), and shows the 100× performance journey that made high-depth simulation
tractable.

**Audience:** Quantum computing practitioners, algorithm designers, CS researchers.

### Proposed post sequence

| # | Working title | Source files | Key idea |
|---|---|---|---|
| 1 | What QAOA Actually Does | `00-foundations.md`, `01-explainer-farhi2014-original-qaoa.md`, `10-qaoa-intuitive-guide.md` | Uniform superposition → problem unitary → mixer unitary → measure. The light-switch analogy. |
| 2 | The Eigenvalue Problem Behind Combinatorial Optimisation | `problem-statement.md`, `00-maths-roadmap.md` | Encode a cost function as a diagonal Hamiltonian; ground state = optimal assignment. |
| 3 | Tensor Networks for QAOA Simulation | `05-tensor-derivation.md`, `02-explainer-basso2021-high-depth.md`, `14-deep-dive-basso2021.md` | The Basso branch-tensor method; hyperindex convention; why tree-like contraction works. |
| 4 | The Walsh-Hadamard Factorisation | `15-wht-factorisation-discovery.md` | **The original contribution.** WHT diagonalises the k-body constraint fold; cost drops from exponential to polynomial in clause width. |
| 5 | From 1× to 100×: A Performance Optimisation Journey | `performance-optimization.md`, `20-post-wht-innovations.md` | Plateau detection, threshold normalisation, swarm/memetic optimiser, Double64 precision. |
| 6 | Global Angles and Parameter Transfer | `11-explainer-p1.3-maxcut-transfer-sources.md`, files in `qaoa-xorsat-research-global-angles-paper/` | Why angles that work for one instance work for many. Concentration phenomena. |
| 7 | Inapproximability: What Quantum Cannot Beat | `09-explainer-tight-inapproximability.md` | Tight bounds on QAOA performance; where classical is provably good enough. |
| 8 | QAOA vs Grover: Two Flavours of Quantum Search | `10-qaoa-intuitive-guide.md` (Grover comparison section) | Structured interference vs brute-force amplitude amplification. |

### Dependencies

Posts 1–2 are prerequisites for everything. Post 3 is prerequisite for 4–5. Posts
6–8 are independent of each other but require 1–5.

---

## Series 2: Hidden Structure (Epsilon Machines & Statistical Learning)

**Source material:** `emic-research/notes/`, `emic/docs/guide/`

**Thesis:** Sequential data has hidden causal structure. Epsilon machines and
spectral learning are two ways to discover it. This series builds the probability
theory, introduces the algorithms, and shows what "computational mechanics" reveals
about complex systems.

**Audience:** Machine learning researchers, data scientists, complexity scientists.

### Proposed post sequence

| # | Working title | Source files | Key idea |
|---|---|---|---|
| 1 | Bayesian Foundations: From Coin Flips to Dirichlet Priors | `bayesian-inference-primer.md` (first half) | Bayes' theorem, conjugate priors, Beta distribution. Build intuition for updating beliefs. |
| 2 | MCMC and Gibbs Sampling: Walking Through Probability Space | `bayesian-inference-primer.md` (second half) | When you cannot compute the posterior analytically, sample from it. Metropolis-Hastings, Gibbs. |
| 3 | What Is an Epsilon Machine? | EMIC guide docs, `complexity-measures-explained.md` | Predictive equivalence classes, causal states, the minimal sufficient statistic of the future given the past. |
| 4 | CSSR: Discovering Causal States From Data | `cssr-deep-dive.md` | The algorithm: hypothesis testing on suffixes, splitting, and merging. Worked example. |
| 5 | Spectral Learning: SVD Meets Hidden Markov Models | `spectral-learning-implementation.md`, `spectral-learning-deep-dive.md` | Hankel matrices, observable operators, why SVD recovers the hidden structure. |
| 6 | Complexity Measures: What They Tell You About Your System | `complexity-measures-explained.md` | Cμ, hμ, excess entropy, crypticity. How to interpret them. |

### Dependencies

Posts 1–2 are Bayesian prerequisites. Post 3 introduces epsilon machines (standalone
if reader knows Bayes). Posts 4–5 are independent algorithms (both require 3).
Post 6 requires 3.

---

## Series 3: Quantum Foundations & Advanced Methods

**Source material:** `pfqe-research/learning/`, `encodings-research/notes/`, `ghl/`

**Thesis:** The mathematical machinery of quantum computing — Hamiltonian simulation,
fermionic encodings, qubitization — rests on a small number of structural ideas.
This series builds them carefully.

**Audience:** Physics-adjacent quantum computing researchers, quantum chemistry
practitioners.

### Proposed post sequence

| # | Working title | Source files | Key idea |
|---|---|---|---|
| 1 | The Schrödinger Equation: From First Principles to Quantum Circuits | `pfqe-research/learning/derivations/schrodinger-foundations.md` | State vectors, propagator, spectral solution, unitarity, Born rule. The bridge from physics to circuits. |
| 2 | Adiabatic State Preparation: A Survey of 36 Papers | `pfqe-research/learning/literature/adiabatic-driver-review.md`, `heisensurvey.md` | Driver Hamiltonians, gap conditions, the zoo of approaches. |
| 3 | Why Smooth Angles Transfer Across Problems | `pfqe-research/learning/derivations/smooth-vqa-transferability.md` | Mele et al.'s insight; why variational angles are not random. |
| 4 | Bravyi-Kitaev Encoding: Mapping Fermions to Qubits | `encodings-research/notes/SRL-study-notes.md` | Jordan-Wigner vs BK, Fenwick trees, the SRL construction, what the star-tree theorem breaks. |
| 5 | Qubitization and Quantum Signal Processing | `ghl/literature_review.md` | Guang Hao Low's framework: block encodings, QSP, QSVT. The unifying abstraction. |

### Dependencies

Posts 1–3 form a sequence (Schrödinger → adiabatic → transferability). Posts 4–5
are independent deep dives (require general QC background but not 1–3).

---

## Series 4: Lessons from the Trenches

**Source material:** Various, cross-cutting concerns.

**Thesis:** Practical lessons from building quantum software: debugging, performance,
education pitfalls.

**Audience:** Broad quantum computing community, educators.

### Proposed post sequence

| # | Working title | Source files | Key idea |
|---|---|---|---|
| 1 | Common Mistakes in Quantum Computing Education | `problem-down/.review/2026-04-16-correctness-audit.md` | 8 high-severity errors found in a QC manuscript. How to not make them. |
| 2 | Python to Julia: Pitfalls in Quantum Software | `qaoa-xorsat/.project/learning/python-to-julia-pitfalls.md` | Type stability, array semantics, performance traps. |
| 3 | Optimiser Selection for Variational Quantum Algorithms | `pfqe-research/learning/literature/optimization-landscape.md` | Nelder-Mead, L-BFGS, INTERP, swarm. When to use what. |

### Dependencies

None — each is standalone.

---

## Publishing cadence

- Current active series: **Linear Algebra for Fun and Profit** (2 parts, both live
  by 2026-07-17), then **The Quantum Bottleneck** (8 parts, 2026-07-28 through
  2026-08-22, twice weekly on Tuesdays and Fridays).
- After Bottleneck completes (late August 2026), begin the next series.
- Recommended order: **QAOA from Scratch** first (strongest original contribution,
  most material ready), then **Hidden Structure**, then **Quantum Foundations**.
- **Lessons from the Trenches** posts can be interleaved as one-offs between series
  or during breaks.

## Agent workflow

For each series, the assigned agent should:

1. **Read all source files** listed in the series table.
2. **Propose refined titles and one-paragraph abstracts** for review.
3. **Draft posts** one at a time, in dependency order.
4. **Generate social hooks** per the social-hook skill after each post is approved.
5. **Place drafts** in `docs/blog/posts/` with future dates (weekly Tuesdays, or as
   directed).
6. **Update this spec** with actual titles, dates, and status as posts are completed.

## Status tracker

| Series | Status | Next action |
|---|---|---|
| Linear Algebra for Fun and Profit | Parts 1-3 live (Part 3 scheduled Jul 21) | Complete |
| The Quantum Bottleneck | 8 parts scheduled (Jul 28 – Aug 22, Tue+Fri) | Auto-publishes |
| QAOA from Scratch | Spec written | Agent: read sources, propose abstracts |
| Hidden Structure | Spec written | Agent: read sources, propose abstracts |
| Quantum Foundations | Spec written | Agent: read sources, propose abstracts |
| Lessons from the Trenches | Spec written | Agent: read sources, propose abstracts |
