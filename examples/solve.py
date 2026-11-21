"""Solve an optimization model with the ProvenDecisions API and print the checked answer.

    pip install requests
    export PROVENDECISIONS_API_KEY=pd_live_...     # create a key in the app: Settings, API keys (Standard and Pro plans)
    python solve.py

The model is typed math, the same as in the web app: one objective, "subject to", one constraint per line.
Every number in the answer comes from a solver and is checked (feasibility, and a dual or KKT certificate)."""
import os

import requests

BASE = "https://proven-decisions.ai"

# Product mix: profit $3 per unit of A and $2 per unit of B; 100 labour hours and 80 units of material.
MODEL = """maximize 3a + 2b
subject to
2a + b <= 100
a + 2b <= 80
a, b >= 0"""


def solve(model, key, base=BASE, session=requests):
    """POST /api/v1/solve; returns the answer as a dict (status, objective, solution, the proof and more)."""
    r = session.post(f"{base}/api/v1/solve", json={"model": model, "depth": 1},
                     headers={"Authorization": f"Bearer {key}"}, timeout=120)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    answer = solve(MODEL, os.environ["PROVENDECISIONS_API_KEY"])
    print("status:   ", answer["status"])
    print("objective:", answer["objective"])
    print("solution: ", answer["solution"])
    print("proof:    ", answer["proof_label"])      # e.g. "Exactly proven optimal"
