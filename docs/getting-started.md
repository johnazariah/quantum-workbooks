# Getting Started

## What you need

1. **Access to a Quokka** — you have two options:
    - **Own a Quokka puck?** Use the [iOS app](https://apps.apple.com/au/app/quokka-quantum/id6754873585) to connect to your puck and load circuits
    - **Don't have one?** [Sign up at quokkacomputing.com](https://www.quokkacomputing.com/get-started) — you'll get access to a Google Colab notebook ("Quokka Start Here") that connects to one of six cloud Quokkas. No hardware needed.
2. **This repo** — for the recipes and explanations

## Set up

**Option A: Quokka Cloud (recommended for most people)**

1. Go to [quokkacomputing.com/get-started](https://www.quokkacomputing.com/get-started) and sign up
2. Click through to the **"Quokka Start Here"** Colab notebook — it walks you through your first quantum program (a "quantum coin" on one qubit)
3. The notebook sends QASM programs to a cloud Quokka and returns the results

There are six cloud Quokkas available:

- `quokka1.quokkacomputing.com` through `quokka6.quokkacomputing.com`

They may occasionally go offline due to power or network conditions — if one is down, try another.

**Option B: Clone the repo locally**

```bash
git clone https://github.com/johnazariah/quantum-workbooks
cd quantum-workbooks/cookbook
```

Browse the recipes, read the explanations, and copy the `.qasm` code into your Quokka Colab notebook or iOS app when you're ready to run.

## Run your first recipe

The Quokka "Start Here" notebook introduces you to QASM with a simple one-qubit "quantum coin" program. Once you're comfortable with that, come back here and try something more interesting.

Open `recipes/01-bell-state/bell.qasm` — you'll see:

```
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
```

Paste this into a code cell in your Quokka Colab notebook (or load it via the iOS app if you have a puck). Run it. You should see outcomes `00` and `11` with roughly equal probability — never `01` or `10`.

Congratulations, you just created an entangled pair of qubits. Now read the [full recipe](recipes/01-bell-state/README.md) to understand *why*.

## How recipes are organized

```
recipes/01-bell-state/
├── README.md        # The explanation — what, why, and how
├── bell.qasm        # The circuit — paste into Quokka
└── expected.txt     # What the output should look like
```

- **Read the README** for the full story
- **Run the `.qasm` file** on your Quokka
- **Check `expected.txt`** to verify your results

## What's OpenQASM 2.0?

[OpenQASM 2.0](https://openqasm.com/) is a simple, standard language for describing quantum circuits. Think of it as assembly language for quantum computers. It looks like this:

```
h q[0];          // put qubit 0 in superposition
cx q[0], q[1];   // entangle qubit 0 and qubit 1
measure q -> c;  // measure and store results
```

It's human-readable, platform-independent, and every quantum computing tool understands it. What you learn here works everywhere.

## Next steps

- **Structured learning?** Follow the [Learning Path](learning-path.md)
- **Just browsing?** Pick any recipe from the [Recipes](recipes/index.md) page
- **Want context?** Check the [References](references.md) for textbooks and courses
