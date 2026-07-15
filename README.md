# Quantum Workbooks

Open quantum computing workbooks, notebooks, and runnable circuit notes.

## Repository layout

```text
cookbook/
  recipes/     # Circuit Bench notes, QASM files, expected outputs, images
  notebooks/   # Companion notebooks for Circuit Bench notes

bottleneck/
  notebooks/   # Runnable companions for The Quantum Bottleneck
  scripts/     # Smoke harnesses and support scripts for exported notebooks
```

## What lives where

- `cookbook/` is the source directory for the Circuit Bench: short, runnable quantum circuits with prose, QASM, and companion notebooks.
- `bottleneck/` is the export surface for *The Quantum Bottleneck*: application-first workbook companions that stay runnable without becoming the manuscript source of truth.

## Current publishing surface

The GitHub Pages build serves the Quantum Workbooks site from `docs/`, including the Circuit Bench and Bottleneck companion surfaces.

## Local preview

Build the site from the repo root:

```bash
pip install mkdocs-material
python3 -m mkdocs serve
```

Run the Bottleneck notebook smoke harness:

```bash
pip install -r bottleneck/requirements.txt
python bottleneck/scripts/notebook_smoke_test.py
```

## License

MIT