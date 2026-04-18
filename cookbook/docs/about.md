# About

## What is The Quokka Cookbook?

A collection of quantum computing recipes — self-contained, problem-first, and executable on [Quokka](https://www.quokkacomputing.com/). Born from the belief that the best way to learn quantum computing is to *run quantum circuits*, not to stare at axioms.

## Who made this?

[John Azariah](https://github.com/johnazariah) — quantum computing student, one of the inventors of the Q# programming language, and someone who struggled with intuition and application of quantum algorithms because he was always bogged down in the maths.

## The teaching philosophy

Most resources teach quantum computing **bottom-up**: start with linear algebra, define qubits, prove properties of gates, build up to algorithms. By the time you reach anything interesting, you've forgotten why you started.

We teach **problem-down**: start with something you want to compute, figure out what circuit solves it, and learn the theory because you need it — not because it's on a syllabus.

Every concept in this cookbook is introduced **at the point where it's useful**, in the context of a working circuit. Phase kickback isn't Chapter 3; it shows up when it saves you a measurement. The QFT isn't a standalone topic; it appears when it solves a problem.

## Why Quokka?

[Quokka](https://www.quokkacomputing.com/) runs standard OpenQASM 2.0. That means:

- **No SDK lock-in.** The circuits are the code. No `import qiskit` boilerplate.
- **Tactile learning.** A physical device makes the abstract concrete.
- **Portable knowledge.** Every `.qasm` file works on any QASM-compatible platform.

Quokka is built by [Eigensystems](https://www.quokkacomputing.com/) in Australia.

## Contributing

This is an open-source project. If you find a bug, want to improve an explanation, or have an idea for a new recipe:

- **Bug or typo?** Open an [issue](https://github.com/johnazariah/quantum-workbooks/issues)
- **New recipe?** Open a [pull request](https://github.com/johnazariah/quantum-workbooks/pulls) following the recipe template
- **Question?** Start a [discussion](https://github.com/johnazariah/quantum-workbooks/discussions)

## License

MIT. Use these recipes however you like.
