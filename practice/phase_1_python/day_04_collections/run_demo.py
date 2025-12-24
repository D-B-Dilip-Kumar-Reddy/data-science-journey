"""
Demo runner for Day 4 collections.

Shows:
- Dictionary-based aggregation
- Set-based uniqueness tracking
"""

from .metrics import aggregate_metrics

sample_execution_stream = [
    "PASS",
    "FAIL",
    "FAIL",
    "CRASH",
    "TIMEOUT",
    "PASS",
    "fail",
    "CRASH",
]


def run():
    print("=== Day 4 Metrics Aggregation Demo ===\n")

    metrics = aggregate_metrics(sample_execution_stream)

    print("Status Counts:")
    for status, count in metrics["counts"].items():
        print(f"{status:>8}: {count}")

    print("\nUnique Failures:")
    for failure in metrics["unique_failures"]:
        print(f"- {failure}")


if __name__ == "__main__":
    run()
