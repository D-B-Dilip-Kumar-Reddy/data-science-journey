from practice.phase_1_python.day_02_conditionals.status_classifier import (
    normalize_status,
    classify_status,
)


def test_normalize_status_basic():
    assert normalize_status("pass") == "PASS"
    assert normalize_status(" FAIL ") == "FAIL"


def test_normalize_status_none():
    assert normalize_status(None) == "UNKNOWN"


def test_classify_known_statuses():
    assert classify_status("PASS") == "PASS"
    assert classify_status("fail") == "FAIL"
    assert classify_status("CRASH") == "CRASH"
    assert classify_status(" timeout ") == "TIMEOUT"


def test_classify_unknown_status():
    assert classify_status("NETWORK_ERROR") == "UNKNOWN"
    assert classify_status("") == "UNKNOWN"
