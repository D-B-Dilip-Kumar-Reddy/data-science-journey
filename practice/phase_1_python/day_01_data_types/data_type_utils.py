"""
Utilities for validating and normalizing basic data types.

These functions represent foundational checks commonly used
in data pipelines and test execution analysis.
"""


def is_valid_execution_time(value) -> bool:
    """
    Check whether execution time is a valid non-negative float.

    Rules:
    - Must be a float
    - Must be >= 0
    """
    return isinstance(value, float) and value >= 0.0


def normalize_status(value) -> str:
    """
    Normalize raw test status values.

    Rules:
    - Accept only strings
    - Strip whitespace
    - Convert to uppercase
    - Return 'UNKNOWN' for invalid input
    """
    if not isinstance(value, str):
        return "UNKNOWN"

    normalized = value.strip().upper()
    return normalized if normalized else "UNKNOWN"
