"""
Quokka helper — send QASM programs to a cloud Quokka and get results.

Usage:
    from quokka_helper import run_qasm, run_qasm_file

    # Run a QASM string
    results = run_qasm("OPENQASM 2.0; ...", shots=1024)

    # Run a .qasm file from the recipes folder
    results = run_qasm_file("../recipes/01-bell-state/bell.qasm", shots=1024)
"""

import json
from pathlib import Path

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Default cloud Quokka — change if one is offline
QUOKKA_HOST = "quokka1"
QUOKKA_URL = f"http://{QUOKKA_HOST}.quokkacomputing.com/qsim/qasm"

# All six cloud Quokkas
ALL_QUOKKAS = [f"quokka{i}" for i in range(1, 7)]


def set_quokka(host: str):
    """Switch to a different cloud Quokka (e.g. 'quokka2')."""
    global QUOKKA_HOST, QUOKKA_URL
    QUOKKA_HOST = host
    QUOKKA_URL = f"http://{host}.quokkacomputing.com/qsim/qasm"


def run_qasm(program: str, shots: int = 1024) -> dict:
    """Send a QASM program to the cloud Quokka and return results."""
    data = {"script": program, "count": shots}
    result = requests.post(QUOKKA_URL, json=data, verify=False)
    result.raise_for_status()
    return json.loads(result.content)


def run_qasm_file(filepath: str, shots: int = 1024) -> dict:
    """Load a .qasm file and run it on the cloud Quokka."""
    program = Path(filepath).read_text()
    return run_qasm(program, shots=shots)
