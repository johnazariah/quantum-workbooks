# Quantum Workbooks — Agent Handoff

> **Project:** Quantum Workbooks — public runnable companions, notebooks, and circuit recipes
> **Owner:** John Azariah (johnazariah)
> **Repo:** https://github.com/johnazariah/quantum-workbooks
> **Site:** GitHub Pages via mkdocs-material — `mkdocs build` from the repo root currently builds the cookbook site served from `cookbook/docs`

---

## What this project is

A public umbrella repo with two surfaces:

1. `cookbook/` — self-contained quantum computing recipes with runnable OpenQASM 2.0 circuits.
2. `bottleneck/` — runnable companion notebooks exported from *The Quantum Bottleneck*.

The tone is conversational but rigorous. No hand-waving, no hype. Runnable artifacts stay explicit and teaching-friendly.

## Current state

### Umbrella structure

- `cookbook/` contains the former flat cookbook repo content.
- `bottleneck/` contains exported Bottleneck notebooks, requirements, and the copied smoke harness.
- Root `mkdocs.yml` currently builds the cookbook site from `cookbook/docs`.

### Cookbook recipe surface

The cookbook contains recipe prose, QASM files, and companion notebooks under `cookbook/`.

### Cookbook site pages

| Page | File |
|------|------|
| Home / Landing | `cookbook/docs/index.md` |
| Getting Started | `cookbook/docs/getting-started.md` |
| Recipe Index | `cookbook/recipes/index.md` |
| Learning Path | `cookbook/docs/learning-path.md` |
| References | `cookbook/docs/references.md` |
| About | `cookbook/docs/about.md` |

### Infrastructure

- `cookbook/docs/recipes` is a symlink to `../recipes`
- `cookbook/docs/javascripts/mathjax.js` exists for math rendering
- `.github/workflows/deploy.yml` deploys the cookbook site via GitHub Pages
- `bottleneck/scripts/notebook_smoke_test.py` validates the exported Bottleneck notebooks in place

## Priority work items

1. **Keep the cookbook content consistent.** Recipe prose, QASM files, and any companion notebooks should agree.
2. **Verify GitHub Pages deployment.** Run `mkdocs build` from the repo root and keep the cookbook site warning-free.
3. **Integrate Bottleneck exports carefully.** `bottleneck/` is downstream runnable material, not the authoritative manuscript source.
4. **Keep runnable code transparent.** Prefer explicit teaching code over opaque helper layers.

## Style guide

- **Tone:** Conversational but precise. No dumbing down, no unnecessary jargon.
- **Math:** KaTeX inline (`$...$`) and display (`$$...$$`). Explain notation in words when it first appears.
- **QASM:** OpenQASM 2.0 only for the cookbook recipe surface.
- **Quokka:** Treat Quokka as a target platform for the cookbook material, not as the identity of the umbrella repo.
- **Bottleneck notebooks:** Keep the code pedagogy-first and directly readable.
- **No hype:** If something requires fault-tolerant QC, say so.

## Related projects

- **[quantum-bottleneck](https://github.com/johnazariah/quantum-bottleneck)** — authoritative manuscript repo for *The Quantum Bottleneck*. `bottleneck/` here is only the runnable export surface.
- **[encodings-book](../encodings-book/)** — fermion-to-qubit encodings textbook. Recipe 08 (VQE for H₂) is a natural on-ramp.
- **[emic](https://github.com/johnazariah/emic)** — epsilon-machine inference library (separate research area).

## Build & preview

```bash
pip install mkdocs-material
mkdocs serve
mkdocs build

pip install -r bottleneck/requirements.txt
python bottleneck/scripts/notebook_smoke_test.py
```