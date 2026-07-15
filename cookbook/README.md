# Circuit Bench

**Quantum circuit notes you can actually run.**

```bash
git clone https://github.com/johnazariah/quantum-workbooks
cd quantum-workbooks/cookbook
```

Pick a circuit note. Read why it matters. Run it on your [Quokka](https://www.quokkacomputing.com/).

## What is this?

A collection of self-contained quantum circuit notes, each built around a real problem and a working [OpenQASM 2.0](https://openqasm.com/) circuit that runs on [Quokka](https://www.quokkacomputing.com/) — a 30-qubit quantum computing system designed for education and exploration.

No framework boilerplate. No 47 imports. Just circuits, explained.

## Circuit notes

| # | Circuit note | What you'll learn |
|---|--------|-------------------|
| 00 | [Reading a Quantum Circuit](recipes/00-reading-a-quantum-circuit/) | Gates, Bloch sphere, unitary rotations, measurement bases |
| 01 | [Bell State](recipes/01-bell-state/) | Entanglement, measurement correlation |
| 02 | [Teleportation](recipes/02-teleportation/) | Classical feedback, the teleportation protocol |
| 03 | [Deutsch-Jozsa](recipes/03-deutsch-jozsa/) | Oracles, quantum speedup, interference |
| ... | More coming | New notes as the workbooks need them |

## How to use this repo

Each note lives in its own directory under `recipes/`:

```
recipes/01-bell-state/
├── README.md        # The explanation — why it matters, how it works
├── bell.qasm        # The circuit — paste into quokka or run from CLI
└── expected.txt     # What you should see
```

Read the README, run the `.qasm` file, compare with `expected.txt`.

## Prerequisites

- A [Quokka](https://www.quokkacomputing.com/) puck, or the Quokka app ([iOS](https://apps.apple.com/au/app/quokka-quantum/id6754873585))
- Curiosity

That's it. Every circuit is a standard OpenQASM 2.0 file — paste it into your Quokka and run. Linear algebra and quantum mechanics are introduced *as needed*, in context, inside each note.

## Contributing

Found a bug in a circuit note? Want to suggest a new one? Open an issue or PR.

## License

MIT
