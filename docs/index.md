---
hide:
  - navigation
---

# The Quokka Cookbook

**Quantum computing recipes you can actually run.**

---

## What is this?

A growing collection of self-contained quantum computing recipes — each one explains a concept from the ground up, builds a circuit step by step, and gives you a working [OpenQASM 2.0](https://openqasm.com/) program you can run on your [Quokka](https://www.quokkacomputing.com/).

No framework bloat. No 47 imports. No prerequisites beyond curiosity. Just circuits, explained — then executed.

## Why we're building this

Most quantum computing resources teach you qubits and gates, then leave you stranded somewhere around phase kickback wondering *why you should care*.

We do it the other way around. Each recipe starts with a **problem** — something concrete and interesting — then builds the quantum circuit that solves it. Theory arrives when it's useful, not when it's scheduled. Phase kickback shows up when it saves you a measurement, not because it's Chapter 3.

The goal is **understanding through doing**. If you can read a `for` loop, you can read a quantum circuit. And if you can run one, you'll understand it better than if you'd read ten pages of formalism.

## What's Quokka?

<div class="grid cards" markdown>

-   :material-cube-outline:{ .lg .middle } **A quantum computer in your hand**

    ---

    [Quokka](https://www.quokkacomputing.com/) is a 30-qubit quantum computing system built by [Eigensystems](https://www.quokkacomputing.com/) in Australia. It's a physical device — a puck that fits in your hand — with a companion [iOS app](https://apps.apple.com/au/app/quokka-quantum/id6754873585) and cloud platform.

    [:octicons-arrow-right-24: www.quokkacomputing.com](https://www.quokkacomputing.com/)

-   :material-file-code-outline:{ .lg .middle } **Standard OpenQASM 2.0**

    ---

    Quokka runs standard [OpenQASM 2.0](https://openqasm.com/) — no proprietary language, no SDK lock-in. Every recipe in this cookbook is a plain text `.qasm` file. What you learn here works everywhere.

</div>

## What's coming

We're releasing recipes regularly, building from the fundamentals to real applications. Each recipe is a self-contained blog post with a runnable circuit.

| | Course | What you'll learn |
|---|--------|-------------------|
| **Appetizers** | Bell state, teleportation, Deutsch-Jozsa | Entanglement, measurement, your first quantum speedup |
| **Mains** | Bernstein-Vazirani, Simon, Grover, QAOA, VQE, QFT | Oracles, search, optimisation, molecular simulation |
| **Desserts** | Phase estimation, error mitigation, quantum counting | The techniques that power the big algorithms |

!!! tip "How each recipe works"

    Every recipe follows the same structure:

    1. **What are we making?** — the problem, in plain language
    2. **Ingredients** — what you need to know (with links if you need a refresher)
    3. **Method** — the circuit, built incrementally with explanation at every step
    4. **Taste test** — run it on your Quokka, see the output, interpret the results
    5. **Chef's notes** — gotchas, deeper connections, and what to try next

## Who is this for?

- **Students** taking a quantum computing course who want a hands-on companion
- **Software engineers** curious about quantum computing but allergic to hype
- **Researchers** who want a quick reference for standard circuits and protocols
- **Anyone** who learns by doing rather than by reading axioms

No physics degree required. We introduce every concept when it's needed, in the context of a working circuit.

## Stay in the loop

Recipes drop regularly. [Watch the repo on GitHub](https://github.com/johnazariah/quokka-cookbook) to get notified, or check back here.

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg .middle } **Learning Path**

    ---

    The full roadmap — what we'll cover and why, in what order.

    [:octicons-arrow-right-24: See the plan](learning-path.md)

-   :material-bookshelf:{ .lg .middle } **References**

    ---

    Textbooks, papers, courses, and talks — curated for going deeper.

    [:octicons-arrow-right-24: Further reading](references.md)

-   :material-github:{ .lg .middle } **Contribute**

    ---

    Found a typo? Want to suggest a recipe? Every recipe is a PR away.

    [:octicons-arrow-right-24: GitHub](https://github.com/johnazariah/quokka-cookbook)

-   :material-cube-outline:{ .lg .middle } **Get a Quokka**

    ---

    The quantum computing puck these recipes are built for.

    [:octicons-arrow-right-24: quokkacomputing.com](https://www.quokkacomputing.com/)

</div>

## Run the recipes — no hardware required

You don't need a physical Quokka puck to follow along. [Sign up at quokkacomputing.com](https://www.quokkacomputing.com/) to get access to Quokka's online servers — paste in any `.qasm` file from this cookbook and run it in your browser.

<!-- TODO: Update signup link and instructions once confirmed with the Quokka team -->

!!! note "Don't have a Quokka yet?"
    Every recipe is a standard OpenQASM 2.0 file. You can also run them for free on:

    - **[IBM Quantum](https://quantum.ibm.com/)** — free account, paste QASM into the Composer, run on simulators or real 127-qubit hardware
    - **[Quirk](https://algassert.com/quirk)** — instant drag-and-drop circuit simulator in the browser (no QASM paste, but great for visual intuition)

    Your learning is portable. What you build here works everywhere.

Every `.qasm` file in this cookbook is a valid OpenQASM 2.0 program. If you outgrow Quokka, the same files run on IBM Quantum, Qiskit, or any other QASM-compatible platform.

