# Quantum Workbooks — Agent Handoff

> **Project:** Quantum Workbooks — public companion site, notebooks, blog support, and circuit notes
> **Owner:** John Azariah (johnazariah)
> **Repo:** https://github.com/johnazariah/quantum-workbooks
> **Site:** GitHub Pages via mkdocs-material — `python3 -m mkdocs build` from the repo root builds the site from `docs/`

---

## What this project is

A public companion surface for *The Quantum Bottleneck* and related quantum teaching material.

1. `bottleneck/` — all runnable companion notebooks for *The Quantum Bottleneck*.
2. `docs/blog/` — blog copy and support material for the quantum sub-blog on `johnazariah.github.io`.
3. `cookbook/` and `docs/recipes/` — the Circuit Bench: self-contained circuit notes with runnable OpenQASM 2.0 material.

The tone is conversational but rigorous. No hand-waving, no hype. Runnable artifacts stay explicit and teaching-friendly.

## Current state

### Umbrella structure

- `docs/` is the MkDocs site surface.
- `bottleneck/` contains the public workbook notebooks, requirements, and smoke harness.
- `docs/bottleneck/index.md` lists the Bottleneck notebooks and companion posts.
- `docs/blog/posts/` contains Bottleneck companion posts and may be used as draft/source material for the quantum sub-blog.
- `cookbook/` contains the source Circuit Bench content and QASM files; `docs/recipes/` is the site-facing Circuit Bench path.

### Circuit Bench surface

The Circuit Bench contains circuit-note prose, QASM files, and companion notebooks under `cookbook/`.

### Site pages

| Page | File |
|------|------|
| Home / Landing | `docs/index.md` |
| Bottleneck notebooks | `docs/bottleneck/index.md` |
| Blog landing | `docs/blog/index.md` |
| Getting Started | `docs/getting-started.md` |
| Circuit Bench Index | `docs/recipes/index.md` |
| Learning Path | `docs/learning-path.md` |
| References | `docs/references.md` |
| About | `docs/about.md` |

### Infrastructure

- `mkdocs.yml` uses `docs_dir: docs`.
- `.github/workflows/deploy.yml` deploys the MkDocs site via GitHub Pages.
- `bottleneck/scripts/notebook_smoke_test.py` validates the exported Bottleneck notebooks in place.

## Priority work items

1. **Keep the Bottleneck companion surface coherent.** The notebooks are the public lab bench for the book.
2. **Keep the Circuit Bench content consistent.** Circuit-note prose, QASM files, and any companion notebooks should agree.
3. **Verify GitHub Pages deployment.** Run `python3 -m mkdocs build` from the repo root when changing docs.
4. **Protect unpublished manuscript text.** Do not copy book prose, derivations, figures, or extended reality-check text into public posts.
5. **Keep runnable code transparent.** Prefer explicit teaching code over opaque helper layers.
6. **Use the Bottleneck/Circuit Bench skill.** For Bottleneck posts or linked circuit side paths, use `.github/skills/bottleneck-circuit-bench/SKILL.md` / `/bottleneck-circuit-bench` so every linked side path is audited before the post is considered done.

## Bottleneck blog guidance

### Role of a companion post

Do not write "the book, but shorter." A companion post should orient the reader to the notebook:

- what real problem motivates the example;
- what classical bottleneck appears;
- what quantum idea enters;
- what the notebook demonstrates;
- what the notebook deliberately simplifies;
- what remains unproven or hardware-limited.

The chapter provides authority. The notebook provides the artifact. The blog provides orientation.

### Tone

Use inviting authority: warm, explanatory, rigorous, and honest. Avoid manifesto-like, combative, or hype-driven phrasing. It is fine to correct bad quantum explanations, but do it by guiding the reader toward the better model rather than arguing with strawmen.

### Structure

The durable Bottleneck rhythm is:

```text
industry hook -> mathematical bottleneck -> quantum algorithm -> worked example/notebook -> reality check
```

For notebook-led blog posts, a good variant is:

```text
real problem -> small notebook model -> concept needed -> circuit/workflow walkthrough -> what this shows and does not show -> what to try next
```

### Manuscript safety

- Do not reuse manuscript paragraphs, figure captions, or derivation sequences.
- Do not reproduce book figures unless explicitly asked and licensed for the public site.
- Cite primary sources directly when making technical or historical claims.
- Treat the manuscript as background authority, not source text to paraphrase.
- It is safe to mention the forthcoming book and link to public companion material.

### Circuit Bench links

Use the Circuit Bench as a just-in-time side path, not as homework. Bottleneck posts are application-first; Circuit Bench notes are optional circuit-building reinforcement when a concept appears.

Do not link a Bottleneck post to a Circuit Bench note until that note has been audited or rewritten to the same pedagogical standard as the post. A linked note should have a small, clear scope; correct gate and parameter conventions; honest claims about what it demonstrates; runnable QASM where applicable; and no hype or sloppy shortcuts. If a note is not publication-quality, fix the note before adding or keeping the link.

Useful links:

| Bottleneck concept | Circuit Bench side path |
|---|---|
| Circuit literacy, gates, Bloch sphere, measurement bases | Circuit Bench 00 — Reading a Quantum Circuit |
| Superposition, CNOT, measurement correlation | Circuit Bench 01 — Bell State |
| Classical feedback / communication | Circuit Bench 02 — Teleportation |
| Oracle/query model and phase kickback | Circuit Bench 03–05 — Deutsch-Jozsa, Bernstein-Vazirani, Simon |
| Amplitude amplification | Circuit Bench 06 — Grover's Search |
| Variational optimisation | Circuit Bench 07–08 — QAOA MaxCut, VQE for H₂ |
| Fourier/period structure | Circuit Bench 09 — Quantum Fourier Transform |
| Eigenphase extraction | Circuit Bench 10 — Quantum Phase Estimation |
| Noise-aware execution | Circuit Bench 11 — Error Mitigation (ZNE) |
| Counting via phase estimation | Circuit Bench 12 — Quantum Counting |

## Style guide

- **Tone:** Conversational but precise. No dumbing down, no unnecessary jargon.
- **Math:** KaTeX inline (`$...$`) and display (`$$...$$`). Explain notation in words when it first appears.
- **QASM:** OpenQASM 2.0 only for the Circuit Bench surface.
- **Quokka:** Treat Quokka as a target platform for the Circuit Bench material, not as the identity of the umbrella repo.
- **Bottleneck notebooks:** Keep the code pedagogy-first and directly readable.
- **No hype:** If something requires fault-tolerant QC, say so.

## Related projects

- **[quantum-bottleneck](https://github.com/johnazariah/quantum-bottleneck)** — authoritative manuscript repo for *The Quantum Bottleneck*. `bottleneck/` here is only the runnable export surface.
- **[encodings-book](../encodings-book/)** — fermion-to-qubit encodings textbook. Circuit Bench 08 (VQE for H₂) is a natural on-ramp.
- **[emic](https://github.com/johnazariah/emic)** — epsilon-machine inference library (separate research area).

## Build & preview

```bash
pip install mkdocs-material
python3 -m mkdocs serve
python3 -m mkdocs build

pip install -r bottleneck/requirements.txt
python bottleneck/scripts/notebook_smoke_test.py
```
