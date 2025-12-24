from practice.phase_1_python.day_03_loops.executor import run_batch


def test_all_pass():
    results = ["PASS", "PASS", "PASS"]
    metrics = run_batch(results)

    assert metrics["PASS"] == 3
    assert metrics["CRASH"] == 0


def test_fail_with_retries_exhausted():
    results = ["FAIL"]
    metrics = run_batch(results, max_retries=1)

    assert metrics["FAIL"] == 1
    assert metrics["RETRIES"] == 2


def test_timeout_retries():
    results = ["TIMEOUT"]
    metrics = run_batch(results, max_retries=2)

    assert metrics["FAIL"] == 1
    assert metrics["RETRIES"] == 3


def test_crash_halts_execution():
    results = ["PASS", "CRASH", "PASS"]
    metrics = run_batch(results)

    assert metrics["CRASH"] == 1
    assert metrics["PASS"] == 1


def test_unknown_status():
    results = ["SOMETHING_ODD"]
    metrics = run_batch(results)

    assert metrics["UNKNOWN"] == 1
