from practice.phase_1_python.day_02_conditionals.rules import decide_action


def test_pass_continues():
    assert decide_action("PASS") == "CONTINUE"


def test_fail_retries():
    assert decide_action("FAIL") == "RETRY"


def test_timeout_retries():
    assert decide_action("TIMEOUT") == "RETRY"


def test_crash_halts():
    assert decide_action("CRASH") == "HALT"


def test_unknown_flags_data():
    assert decide_action("UNKNOWN") == "FLAG_DATA"
    assert decide_action(None) == "FLAG_DATA"
