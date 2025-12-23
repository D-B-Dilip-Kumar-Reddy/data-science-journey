"""
Demo runner for Day 2 conditional logic.

This script simulates multiple test executions
and shows how decision logic is applied.
"""

from rules import decide_action

sample_results = [
    "PASS",
    "FAIL",
    "CRASH",
    " timeout ",
    "unknown_status",
    None
]


def run():
    for idx, result in enumerate(sample_results, start=1):
        action = decide_action(result)
        print(f"Iteration {idx}: status={result} -> action={action}")


if __name__ == "__main__":
    run()
