# Bottleneck Workbooks

This directory is the runnable companion surface for *The Quantum Bottleneck*.

## What is here

- `notebooks/` contains the eight companion notebooks.
- `scripts/notebook_smoke_test.py` is the smoke harness copied from the book repo so the exported notebooks can still be checked in place.

## What is not here

- The full book manuscript is still authored in the authoritative `quantum-bottleneck` repo.
- The Quokka Cookbook materials have not been migrated yet.

## Pedagogy note

The notebook code is intentionally transparent rather than abstracted behind polished helper layers. That is a teaching choice: readers should be able to see the circuit construction, API calls, and post-processing directly.

## Local use

Install the local notebook environment:

```bash
pip install -r requirements.txt
```

Run the copied smoke harness from this directory:

```bash
python scripts/notebook_smoke_test.py
```

## Canonical source

Treat this directory as an export surface for runnable companions. If notebook content and book prose drift, the book repo wins.
