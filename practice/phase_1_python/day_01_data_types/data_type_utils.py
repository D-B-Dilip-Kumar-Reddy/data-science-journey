"""
Utility functions for validating and normalizing basic data types.

These utilities represent foundational checks used in
automotive center-stack stability data pipelines.

This module contains PURE logic:
- No printing
- No side effects
- Fully testable
"""


def is_valid_execution_time(value) -> bool:
    """
    Validate execution duration.

    Rules:
    - Must be a float
    - Must be non-negative

    Rationale:
    Execution time is used for:
    - Threshold checks
    - Trend analysis
    - Percentile calculations
    """
    return isinstance(value, float) and value >= 0.0


def normalize_status(value) -> str:
    """
    Normalize raw test status values.

    Rules:
    - Accept only strings
    - Trim whitespace
    - Convert to uppercase
    - Return 'UNKNOWN' for invalid or empty input

    Supported conceptual states:
    PASS, FAIL, CRASH, TIMEOUT, UNKNOWN
    """
    if not isinstance(value, str):
        return "UNKNOWN"

    normalized = value.strip().upper()
    return normalized if normalized else "UNKNOWN"
