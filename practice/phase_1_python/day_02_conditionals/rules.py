"""
Decision rules for execution handling.

This module decides what action the test system
should take based on classified execution outcomes.

Responsibilities:
- Map execution state → system action
- Contain business / safety rules
"""

from .status_classifier import classify_status


def decide_action(status) -> str:
    """
    Decide next action based on execution status.

    Returns one of:
    CONTINUE   -> proceed normally
    RETRY      -> retry execution
    HALT       -> stop execution immediately
    FLAG_DATA  -> mark data quality issue
    """
    classification = classify_status(status)

    if classification == "PASS":
        return "CONTINUE"

    if classification == "FAIL":
        return "RETRY"

    if classification == "TIMEOUT":
        return "RETRY"

    if classification == "CRASH":
        return "HALT"

    return "FLAG_DATA"
