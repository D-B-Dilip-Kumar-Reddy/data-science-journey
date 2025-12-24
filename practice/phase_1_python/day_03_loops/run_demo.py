"""
Demo runner for Day 3 loops.

Shows:
- Batch execution
- Controlled retries
- Aggregated metrics
"""

from .executor import run_batch

sample_execution_stream = [
    "PASS",
    "FAIL",
    "FAIL",
    "TIMEOUT",
    "PASS",
    "CRASH",
    "PASS",  # will never be reached
]


def run():
    print("=== Day 3 Batch Execution Demo ===\n")
    metrics = run_batch(sample_execution_stream, max_retries=2)

    print("Aggregated Metrics:")
    for key, value in metrics.items():
        print(f"{key:>8}: {value}")


if __name__ == "__main__":
    run()
