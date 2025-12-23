"""
Status classification logic.

This module converts raw test execution status into
normalized, decision-ready outcomes.
"""

VALID_STATUSES = {"PASS", "FAIL", "CRASH", "TIMEOUT"}


def normalize_status(status: str) -> str:
    """
    Normalize raw status input.

    - Strips whitespace
    - Converts to uppercase
    - Handles None safely
    """
    if status is None:
        return "UNKNOWN"

    return status.strip().upper()


def classify_status(status: str) -> str:
    """
    Classify execution status into known categories.

    Returns:
        One of: PASS, FAIL, CRASH, TIMEOUT, UNKNOWN
    """
    normalized = normalize_status(status)

    if normalized in VALID_STATUSES:
        return normalized

    return "UNKNOWN"
