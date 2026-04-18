# Quantum Workbooks

Open quantum computing workbooks, notebooks, and runnable circuit recipes.

## Repository layout

```text
cookbook/
  docs/        # MkDocs site for the runnable OpenQASM recipe collection
  recipes/     # Recipe posts, QASM files, expected outputs, images
  notebooks/   # Companion notebooks for cookbook recipes

bottleneck/
  notebooks/   # Runnable companions for The Quantum Bottleneck
  scripts/     # Smoke harnesses and support scripts for exported notebooks
```

## What lives where

- `cookbook/` is the existing recipe collection: short, runnable quantum circuits with prose, QASM, and companion notebooks.
- `bottleneck/` is the export surface for *The Quantum Bottleneck*: application-first workbook companions that stay runnable without becoming the manuscript source of truth.

## Current publishing surface

The GitHub Pages build currently serves the cookbook site while the umbrella repo structure settles.

## Local preview

Build the cookbook site from the repo root:

```bash
pip install mkdocs-material
mkdocs serve
```

Run the Bottleneck notebook smoke harness:

```bash
pip install -r bottleneck/requirements.txt
python bottleneck/scripts/notebook_smoke_test.py
```

## License

MIT