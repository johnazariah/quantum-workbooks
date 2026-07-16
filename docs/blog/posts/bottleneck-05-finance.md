---
date: 2026-08-12
notebook: "https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/05-finance.ipynb"
categories:
  - The Quantum Bottleneck
  - Finance
tags:
  - Monte Carlo
  - quantum amplitude estimation
  - option pricing
  - phase estimation
authors:
  - John Azariah
---

# The Convergence Wall

**Finance often asks for an average over possible futures. Classical Monte Carlo is the workhorse for that job, but every extra digit of accuracy is expensive.**

<!-- more -->

An option price, a value-at-risk estimate, a stress test, and an exposure calculation all have the same basic shape: define a model for uncertain market moves, run many scenarios, compute the payoff or loss in each scenario, and average.

That is a good reason Monte Carlo is everywhere in finance. It is flexible, model-agnostic, and embarrassingly parallel. If the payoff has path dependence, early exercise, barriers, correlations, or a messy book of instruments, Monte Carlo usually still has a way in.

The catch is convergence.

## The bottleneck: square-root accuracy

For a European call option, the quantity of interest is an expectation:

$$
V = e^{-rT}\mathbb{E}[\max(S_T - K, 0)].
$$

The Black-Scholes formula gives a closed-form answer under its assumptions, which makes it a useful benchmark. But the Monte Carlo version is the more general pattern:

1. sample possible terminal prices $S_T$;
2. compute the payoff $\max(S_T - K, 0)$;
3. average the discounted payoff.

If the payoff samples have standard deviation $\sigma$, then the Monte Carlo standard error scales like

$$
\frac{\sigma}{\sqrt{N}},
$$

where $N$ is the number of sampled scenarios. To halve the error, you need roughly four times as many paths. To gain another decimal digit, you need roughly one hundred times as many paths.

That is the convergence wall. It is not that Monte Carlo is bad. It is that the last bit of accuracy gets brutally expensive.

## The quantum idea: estimate an amplitude

Quantum Amplitude Estimation, or QAE, attacks the square-root law. In its ideal form, if a quantum circuit prepares a probability amplitude $a$ encoding the quantity of interest, QAE can estimate $a$ with error scaling like $1/N$ rather than $1/\sqrt{N}$.

That is the famous quadratic improvement.

The word "if" is doing real work. A finance problem does not arrive already encoded as a clean quantum amplitude. A useful QAE pipeline needs circuits for the uncertainty model, payoff function, comparison threshold, and controlled amplification operator. Those circuits have to be accurate enough that the asymptotic improvement is not eaten by encoding cost.

The companion notebook therefore narrows the scope. It does not build a production option-pricing oracle. It shows the convergence issue classically, then uses a compiled toy phase-readout circuit to make the QAE mechanism visible.

If the phase-readout part is the unfamiliar piece, [Circuit Bench 10: Quantum Phase Estimation](../../circuit-bench/10-quantum-phase-estimation/README.md) gives the gate-level pattern: controlled powers, inverse QFT, and a binary phase estimate.

## The companion notebook

The notebook has two deliberately separate halves.

First, it prices a simple Black-Scholes call option both analytically and by classical Monte Carlo. This gives you the baseline and the convergence picture:

```python
for n_paths in path_counts:
    estimate = monte_carlo_call_price(n_paths)
    error = abs(estimate - black_scholes_price)
```

Second, it switches to a toy quantum proxy. Instead of encoding the full payoff distribution, it discretises the terminal-price model into a binary exercise-probability question: is the option in the money or not? That probability is mapped onto a three-bit phase grid, and a compiled amplitude-estimation-style circuit reads out the corresponding phase.

That scope is important:

- the notebook uses Black-Scholes and Monte Carlo for the actual option-pricing baseline;
- the quantum circuit estimates a discretised exercise-probability proxy, not the full discounted payoff;
- the amplitude-estimation circuit is compiled from the known proxy value;
- the state-preparation, payoff, and controlled-Grover oracles are not constructed.

So the notebook is not claiming to quantum-price an option. It is showing why Monte Carlo convergence hurts, and what kind of phase-estimation readout sits inside QAE once the hard oracle-building work has been done.

## Reality check

The finance story is tempting to oversell because the asymptotic improvement is real and easy to state. Quadratic speedups are valuable in a domain that spends huge resources on Monte Carlo.

But useful quantum finance has to pay for the whole pipeline.

First, the probability distribution must be loaded or generated coherently. If preparing the market model costs too much, the algorithm loses before estimation starts.

Second, the payoff must be encoded reversibly. Real derivatives can have path dependence, discontinuities, early exercise logic, and book-level netting rules. Turning those into quantum circuits is engineering, not notation.

Third, amplitude estimation usually needs deeper controlled circuits than near-term hardware can run reliably. The cleanest version is a fault-tolerant algorithm, not a shallow demonstration circuit.

The honest claim is therefore narrow but worth understanding: QAE changes the scaling of expectation estimation once a suitable quantum encoding exists. The notebook shows the convergence wall and the phase-readout mechanism in miniature. The bottleneck is building the full financial oracle cheaply enough for that scaling to matter.

## Want more?

The [companion notebook](https://github.com/johnazariah/quantum/blob/main/bottleneck/notebooks/05-finance.ipynb) lets you compare Black-Scholes, Monte Carlo convergence, and a compiled three-bit amplitude-estimation proxy. For the phase-estimation circuit pattern underneath the proxy, see [Circuit Bench 10 — Quantum Phase Estimation](../../circuit-bench/10-quantum-phase-estimation/README.md).

---

*This is Unit 5 of The Quantum Bottleneck series. Next up: [The Scheduling Nightmare](bottleneck-06-supply-chains.md) — when optimisation means finding a good discrete assignment under competing constraints.*
