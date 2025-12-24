"""
Demo runner for Day 1 data type utilities.

Purpose:
- Demonstrate how raw center-stack stability data
  is validated and normalized before analysis
- Provide a human-readable sanity check

This file is NOT used in pipelines or tests.
It exists only to demonstrate behavior.
"""

from data_type_utils import is_valid_execution_time, normalize_status

sample_execution_times = [1.2, -0.5, 5, "10.0", None]
sample_statuses = ["pass", " FAIL ", "", None, 404]


def run():
    print("=== Execution Time Validation ===")
    for value in sample_execution_times:
        print(f"{value!r:>8} -> valid={is_valid_execution_time(value)}")

    print("\n=== Status Normalization ===")
    for status in sample_statuses:
        print(f"{status!r:>8} -> normalized={normalize_status(status)}")


if __name__ == "__main__":
    run()
