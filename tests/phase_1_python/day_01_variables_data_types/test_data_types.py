from practice.phase_1_python.day_01_data_types.data_type_utils import (
    is_valid_execution_time,
    normalize_status,
)


def test_valid_execution_time():
    assert is_valid_execution_time(0.0) is True
    assert is_valid_execution_time(0.5) is True
    assert is_valid_execution_time(10.25) is True


def test_invalid_execution_time():
    assert is_valid_execution_time(-1.0) is False
    assert is_valid_execution_time(5) is False
    assert is_valid_execution_time("5.0") is False
    assert is_valid_execution_time(None) is False


def test_normalize_status_valid_inputs():
    assert normalize_status("pass") == "PASS"
    assert normalize_status(" FAIL ") == "FAIL"
    assert normalize_status("CrAsH") == "CRASH"


def test_normalize_status_invalid_inputs():
    assert normalize_status("") == "UNKNOWN"
    assert normalize_status(None) == "UNKNOWN"
    assert normalize_status(123) == "UNKNOWN"
