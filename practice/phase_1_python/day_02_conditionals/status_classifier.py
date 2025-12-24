"""
Status classification utilities.

This module converts raw execution outcomes from
automotive center-stack stability tests into
normalized, well-defined categories.

Responsibilities:
- Normalize raw input
- Classify into known execution states
- Never make decisions
"""

VALID_STATUSES = {"PASS", "FAIL", "CRASH", "TIMEOUT"}


def normalize_status(value) -> str:
    """
    Normalize raw status input.

    Rules:
    - Accept only strings
    - Strip whitespace
    - Convert to uppercase
    - Return 'UNKNOWN' for invalid or empty input
    """
    if not isinstance(value, str):
        return "UNKNOWN"

    normalized = value.strip().upper()
    return normalized if normalized else "UNKNOWN"


def classify_status(value) -> str:
    """
    Classify execution status into a known category.

    Returns one of:
    PASS, FAIL, CRASH, TIMEOUT, UNKNOWN
    """
    normalized = normalize_status(value)

    if normalized in VALID_STATUSES:
        return normalized

    return "UNKNOWN"
