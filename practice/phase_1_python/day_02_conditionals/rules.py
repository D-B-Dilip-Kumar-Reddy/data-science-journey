"""
Decision rules for execution handling.

This module defines what action should be taken
based on classified execution outcomes.
"""

from .status_classifier import classify_status


def decide_action(status: str) -> str:
    """
    Decide pipeline action based on execution status.

    Returns:
        CONTINUE
        RETRY
        HALT
        FLAG_DATA
    """
    classification = classify_status(status)

    if classification == "PASS":
        return "CONTINUE"

    if classification == "FAIL":
        return "RETRY"

    if classification == "CRASH":
        return "HALT"

    if classification == "TIMEOUT":
        return "RETRY"

    return "FLAG_DATA"
