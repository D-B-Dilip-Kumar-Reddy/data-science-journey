"""
Demo runner for Day 2 conditional logic.

Purpose:
- Show how raw execution results are classified
- Show what action the system would take
- Human-readable sanity check only
"""

from .rules import decide_action

sample_results = [
    "PASS",
    " fail ",
    "CRASH",
    "timeout",
    "",
    None,
    "random_error"
]


def run():
    print("=== Day 2 Conditional Logic Demo ===\n")
    for idx, result in enumerate(sample_results, start=1):
        action = decide_action(result)
        print(f"Iteration {idx}: status={result!r:>12} -> action={action}")


if __name__ == "__main__":
    run()
