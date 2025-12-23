"""
Demo runner for Day 1 data type utilities.

This script demonstrates how raw execution data
is validated and normalized before analysis.
"""

from data_type_utils import is_valid_execution_time, normalize_status

sample_execution_times = [1.2, -1.0, 5, "10.0", None]
sample_statuses = ["pass", " FAIL ", "", None, 123]


def run():
    print("Execution Time Validation")
    for value in sample_execution_times:
        print(f"{value!r} -> valid={is_valid_execution_time(value)}")

    print("\nStatus Normalization")
    for status in sample_statuses:
        print(f"{status!r} -> {normalize_status(status)}")


if __name__ == "__main__":
    run()
