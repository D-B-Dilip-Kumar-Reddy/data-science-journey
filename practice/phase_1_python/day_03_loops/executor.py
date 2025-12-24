"""
Batch execution engine for center-stack stability testing.

Responsibilities:
- Run iterations in a loop
- Apply retry rules
- Aggregate execution metrics
"""

from practice.phase_1_python.day_02_conditionals.rules import decide_action


def run_batch(execution_results, max_retries=2):
    """
    Run batch execution with controlled retries.

    Args:
        execution_results: iterable of raw execution statuses
        max_retries: max retries allowed for FAIL/TIMEOUT

    Returns:
        metrics dict with aggregated results
    """
    metrics = {
        "PASS": 0,
        "FAIL": 0,
        "CRASH": 0,
        "TIMEOUT": 0,
        "RETRIES": 0,
        "UNKNOWN": 0,
    }

    for status in execution_results:
        retries = 0

        while True:
            action = decide_action(status)

            if action == "CONTINUE":
                metrics["PASS"] += 1
                break

            if action == "RETRY":
                retries += 1
                metrics["RETRIES"] += 1

                if retries > max_retries:
                    metrics["FAIL"] += 1
                    break

            elif action == "HALT":
                metrics["CRASH"] += 1
                return metrics

            else:
                metrics["UNKNOWN"] += 1
                break

    return metrics
