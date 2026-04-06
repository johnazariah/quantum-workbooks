# The Quokka Cookbook

**Quantum computing recipes you can actually run.**

```bash
git clone https://github.com/johnazariah/quokka-cookbook
pip install quokka
quokka recipes/01-bell-state/bell.qasm
```

Pick a recipe. Read why it matters. Run it.

---

## What is this?

A collection of self-contained quantum computing recipes, each built around a real problem and a working [OpenQASM 2.0](https://openqasm.com/) circuit that runs on [quokka](https://github.com/XXX/quokka).

No framework boilerplate. No 47 imports. Just circuits, explained.

## How to use

Each recipe lives in its own directory:

```
recipes/01-bell-state/
├── README.md        # The blog post
├── bell.qasm        # The circuit
└── expected.txt     # What you should see
```

Read the README, run the `.qasm` file, compare with `expected.txt`. That's it.

## Browse the recipes

| # | Recipe | What you'll learn |
|---|--------|-------------------|
| 01 | [Bell State](../recipes/01-bell-state/README.md) | Entanglement, measurement correlation |
| 02 | [Teleportation](../recipes/02-teleportation/README.md) | Classical feedback, the teleportation protocol |
| 03 | [Deutsch-Jozsa](../recipes/03-deutsch-jozsa/README.md) | Oracles, quantum speedup, interference |
