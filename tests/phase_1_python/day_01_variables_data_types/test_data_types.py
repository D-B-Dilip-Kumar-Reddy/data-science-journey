from practice.phase_1_python.day_01_data_types.data_type_utils import (
    is_valid_execution_time,
    normalize_status,
)


# -----------------------------
# Execution Time Validation
# -----------------------------

def test_execution_time_valid_float():
    assert is_valid_execution_time(0.0) is True
    assert is_valid_execution_time(0.5) is True
    assert is_valid_execution_time(12.75) is True


def test_execution_time_invalid_negative():
    assert is_valid_execution_time(-0.1) is False
    assert is_valid_execution_time(-10.0) is False


def test_execution_time_invalid_type():
    assert is_valid_execution_time(5) is False          # int
    assert is_valid_execution_time("5.0") is False      # str
    assert is_valid_execution_time(None) is False        # None


# -----------------------------
# Status Normalization
# -----------------------------

def test_normalize_status_valid_strings():
    assert normalize_status("pass") == "PASS"
    assert normalize_status(" FAIL ") == "FAIL"
    assert normalize_status("CrAsH") == "CRASH"
    assert normalize_status(" timeout ") == "TIMEOUT"


def test_normalize_status_empty_or_whitespace():
    assert normalize_status("") == "UNKNOWN"
    assert normalize_status("   ") == "UNKNOWN"


def test_normalize_status_invalid_type():
    assert normalize_status(None) == "UNKNOWN"
    assert normalize_status(404) == "UNKNOWN"
    assert normalize_status([]) == "UNKNOWN"
