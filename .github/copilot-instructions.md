# Quokka Cookbook — Agent Handoff

> **Project:** The Quokka Cookbook — quantum computing recipes you can actually run
> **Owner:** John Azariah (johnazariah)
> **Repo:** https://github.com/johnazariah/quokka-cookbook
> **Platform:** [Quokka](https://www.quokkacomputing.com/) — a 30-qubit quantum computing puck by Eigensystems (Chris Ferrie & Simon Devitt). It runs standard OpenQASM 2.0 programs.
> **Site:** GitHub Pages via mkdocs-material — `mkdocs build` to build, `mkdocs serve` to preview

---

## What this project is

A blog-style collection of self-contained quantum computing recipes. Each recipe:
1. Explains a quantum concept or algorithm, problem-first
2. Builds a circuit step-by-step in prose
3. Provides a runnable `.qasm` file (OpenQASM 2.0) that works on Quokka
4. Follows a fixed template: **What are we making? → Ingredients → Method → Taste test → Chef's notes**

The tone is conversational but rigorous. No hand-waving, no hype. Every claim is backed by a circuit you can run.

## Current state

### Recipes — 12 planned, varying completeness

| # | Recipe | README | QASM | Status |
|---|--------|--------|------|--------|
| 01 | Bell State | ✅ 279 lines | ✅ bell.qasm | **Complete** |
| 02 | Teleportation | ❌ placeholder (9 lines) | ✅ teleport.qasm | **Needs write-up** |
| 03 | Deutsch-Jozsa | ❌ placeholder (9 lines) | ✅ 2 qasm files | **Needs write-up** |
| 04 | Bernstein-Vazirani | ✅ 231 lines | ✅ | Complete |
| 05 | Simon's Problem | ✅ 230 lines | ✅ | Complete |
| 06 | Grover's Search | ✅ 286 lines | ✅ | Complete |
| 07 | QAOA MaxCut | ✅ 267 lines | ✅ | Complete |
| 08 | VQE for H₂ | ✅ 208 lines | ✅ | Complete |
| 09 | QFT | ✅ 226 lines | ✅ | Complete |
| 10 | QPE | ✅ 234 lines | ✅ | Complete |
| 11 | Error Mitigation (ZNE) | ✅ 212 lines | ✅ 3 qasm files | Complete |
| 12 | Quantum Counting | ✅ 211 lines | ✅ | Complete |

### Site pages

| Page | File | Status |
|------|------|--------|
| Home / Landing | `docs/index.md` | ✅ Complete |
| Getting Started | `docs/getting-started.md` | ✅ Written |
| Recipe Index | `recipes/index.md` | ✅ Written |
| Learning Path | `docs/learning-path.md` | ✅ Written |
| References | `docs/references.md` | ✅ Written |
| About | `docs/about.md` | ✅ Written |

### mkdocs nav

The individual recipe nav entries are **commented out** in `mkdocs.yml`. This was intentional — uncommenting them publishes the recipes. The flat `Recipes: recipes/index.md` entry is the current live nav item.

### Infrastructure

- `docs/recipes` is a **symlink** to `recipes/` at the repo root (so mkdocs can find them)
- `docs/javascripts/mathjax.js` exists for math rendering
- `.github/workflows/` has a GitHub Actions deploy workflow (may need verification)
- No devcontainer yet

## Priority work items

1. **Write Recipe 02 (Teleportation) and Recipe 03 (Deutsch-Jozsa).** The QASM files exist; the write-ups need to match the style and depth of Recipe 01. Use Recipe 01 as the gold standard for tone, structure, and level of detail.

2. **Review all recipes for consistency.** Ensure every recipe follows the template: What are we making? → Ingredients → Background → Method → Taste test → Chef's notes.

3. **Uncomment mkdocs nav entries** once recipes are reviewed and ready to publish.

4. **Verify GitHub Pages deployment.** Run `mkdocs build` — it should produce a clean build with no warnings (some warnings about missing recipe READMEs were previously fixed with placeholders).

5. **Replace remaining `XXX` placeholders.** Some files may still reference `https://github.com/XXX/quokka` — replace with `https://www.quokkacomputing.com/`.

## Recipe template

Every recipe README must follow this structure:

```markdown
# Recipe NN: Title

## What are we making?
(1 paragraph — the problem, why it matters, no jargon)

## Ingredients
(bullet list: qubit count, gates used, prerequisites with links)

## Background: [contextual heading]
(the classical intuition — coins, cards, whatever makes it click)

## Method
### Step 1: ...
### Step 2: ...
(build the circuit incrementally, explain every gate, show the math with KaTeX)

## The complete circuit
(full QASM listing, inline and linked to the .qasm file)
(ASCII circuit diagram)

## Taste test
(how to run it, expected output, what to look for)

## Chef's notes
(gotchas, connections to other recipes, deeper references, "if you liked this try...")
```

## Style guide

- **Tone:** Conversational but precise. "We" voice. No dumbing down, no unnecessary jargon.
- **Math:** KaTeX inline (`$...$`) and display (`$$...$$`). Always explain what the notation means in words immediately after introducing it.
- **Circuits:** Every recipe includes an ASCII circuit diagram AND a `.qasm` file.
- **QASM:** OpenQASM 2.0 only. Every file must start with `OPENQASM 2.0;` and `include "qelib1.inc";`. Keep circuits under 50 lines for early recipes.
- **Quokka:** Always refer to it as "Quokka" (capital Q) and link to https://www.quokkacomputing.com/. Never say `pip install quokka`. It's a physical device — users load QASM via the Quokka app.
- **Cross-references:** Link to other recipes by relative path: `[Recipe 01](../01-bell-state/README.md)`.
- **No hype:** If something requires fault-tolerant QC, say so.

## Related projects

- **[problem-down](https://github.com/johnazariah/problem-down)** — companion "Book A" project: application-oriented quantum computing, one industry problem per chapter. The Cookbook is "Book B" (how to build circuits); problem-down is "Book A" (why you should care).
- **[encodings-book](../encodings-book/)** — the existing fermion-to-qubit encodings textbook. Recipe 08 (VQE for H₂) is a natural on-ramp.
- **[emic](https://github.com/johnazariah/emic)** — epsilon-machine inference library (separate research area).

## Build & preview

```bash
pip install mkdocs-material
mkdocs serve        # preview at http://127.0.0.1:8000
mkdocs build        # build to site/
mkdocs gh-deploy    # deploy to GitHub Pages
```
