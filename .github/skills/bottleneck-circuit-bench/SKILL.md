---
name: bottleneck-circuit-bench
description: Use when writing, revising, or reviewing Bottleneck companion posts, companion notebooks, or linked Circuit Bench/Cookbook material in quantum-workbooks. Ensures each Bottleneck post is application-first and every linked circuit side path is audited before publication.
---

# Bottleneck + Circuit Bench workflow

Use this skill whenever the task involves:

- a Bottleneck companion blog post;
- a Bottleneck workbook or notebook landing page;
- a Circuit Bench/Cookbook page, notebook, or QASM file that may be linked from Bottleneck material;
- deciding whether a Bottleneck post is ready to publish.

## Core rule

The Bottleneck post is the main path. Circuit Bench material is an optional side path for readers who want to inspect the circuit machinery.

Do not add or keep a link from a Bottleneck post to a Circuit Bench page until that side path has been audited or rewritten to publication quality. A Bottleneck post is not done if one of its linked circuit side paths is still sloppy, misleading, inconsistent with the notebook, or overclaims what the circuit demonstrates.

## Workflow

1. Start from the Bottleneck reader journey.
   - Identify the real problem, the classical bottleneck, the quantum idea, the companion notebook, and the intended reality check.
   - Keep the post application-first. Do not turn the post into a gate tutorial.

2. Identify just-in-time circuit side paths.
   - List only the circuit concepts the post actually uses.
   - Link Circuit Bench pages only where they help the reader at the moment a concept appears.
   - Do not make Circuit Bench material a prerequisite or homework.

3. Audit every linked side path before declaring the Bottleneck work done.
   - Check the page prose, any companion notebook, and any QASM file together.
   - Verify gate order, parameter conventions, measurement basis, register naming, and claimed output distributions agree across surfaces.
   - Confirm QASM is OpenQASM 2.0 on the public circuit surface.
   - Prefer plain Markdown for Circuit Bench pages so they read cleanly in GitHub, IDEs, and MkDocs. Avoid MkDocs-only collapsibles such as `??? abstract` unless the user explicitly asks for them.

4. Fix or remove weak links.
   - If the side path is publication-quality after small edits, fix it and keep the link.
   - If the side path needs a larger rewrite, either do the rewrite now or remove/delay the link.
   - Do not leave a Bottleneck post pointing at unaudited legacy recipe material.

5. Validate the public surface.
   - For documentation/site changes, run `python3 -m mkdocs build` from the repository root.
   - For notebook changes, at minimum confirm the notebook JSON loads and code cells parse; run the relevant smoke harness when appropriate.
   - For QASM changes, check syntax and conventions against the corresponding prose/notebook.

## Pedagogical standard

Use the same standard for Bottleneck posts and Circuit Bench pages:

- warm, conversational, technically precise;
- no quantum hype and no vague advantage claims;
- honest about what the circuit demonstrates and what it does not;
- explicit about measurement basis and interpretation;
- clear notation introduced before use;
- no copied manuscript prose, derivation sequences, or unpublished figures;
- runnable artifacts stay transparent rather than hidden behind opaque helper layers.

Good Circuit Bench pages have a small scope. They answer: what circuit is being built, why the gates are there, what a run should show, what would count as a misconception, and where the demonstration stops.

## Naming and tone

Use "Circuit Bench" as the user-facing frame for new or revised prose unless the user asks otherwise. Treat `cookbook/` and `docs/recipes/` as current implementation paths and legacy URLs until a full repository rename is requested.

Avoid cute cookbook metaphors in new or rewritten material. Prefer direct headings such as "What this circuit does", "Circuit walkthrough", "Run it", "What this shows", and "What this does not show".

## Useful side-path map

| Bottleneck concept | Circuit Bench side path |
|---|---|
| Circuit literacy, gates, Bloch sphere, measurement bases | Circuit Bench 00 — Reading a Quantum Circuit |
| Superposition, CNOT, measurement correlation | Circuit Bench 01 — Bell State |
| Classical feedback / communication | Circuit Bench 02 — Teleportation |
| Oracle/query model and phase kickback | Circuit Bench 03–05 — Deutsch-Jozsa, Bernstein-Vazirani, Simon |
| Amplitude amplification | Circuit Bench 06 — Grover's Search |
| Variational optimisation | Circuit Bench 07–08 — QAOA MaxCut, VQE for H2 |
| Fourier/period structure | Circuit Bench 09 — Quantum Fourier Transform |
| Eigenphase extraction | Circuit Bench 10 — Quantum Phase Estimation |
| Noise-aware execution | Circuit Bench 11 — Error Mitigation / ZNE |
| Counting via phase estimation | Circuit Bench 12 — Quantum Counting |

## Known pitfalls to catch

- Z-basis Bell counts alone show correlation, not non-classicality. If coherence matters, add or discuss an X-basis check; do not overclaim.
- QAOA angles must state the convention. If the notebook uses `rz(2 * gamma)` and `rx(2 * beta)`, the QASM comments and values must match that convention.
- Small toy demonstrations do not establish practical quantum advantage. Say when fault tolerance, scale, or hardware quality remains the limiting factor.
