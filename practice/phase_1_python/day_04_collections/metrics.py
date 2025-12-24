"""
Metrics aggregation utilities for center-stack stability testing.

Responsibilities:
- Aggregate execution status counts
- Track unique failure types
"""

from practice.phase_1_python.day_02_conditionals.status_classifier import classify_status


def aggregate_metrics(execution_results):
    """
    Aggregate stability metrics from execution results.

    Args:
        execution_results: iterable of raw execution statuses

    Returns:
        dict containing counts and unique failures
    """
    metrics = {
        "counts": {
            "PASS": 0,
            "FAIL": 0,
            "CRASH": 0,
            "TIMEOUT": 0,
            "UNKNOWN": 0,
        },
        "unique_failures": set(),
    }

    for raw_status in execution_results:
        status = classify_status(raw_status)
        metrics["counts"][status] += 1

        if status in {"FAIL", "CRASH"}:
            metrics["unique_failures"].add(status)

    return metrics
