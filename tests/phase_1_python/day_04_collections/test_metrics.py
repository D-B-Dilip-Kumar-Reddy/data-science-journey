from practice.phase_1_python.day_04_collections.metrics import aggregate_metrics


def test_basic_aggregation():
    results = ["PASS", "FAIL", "PASS"]
    metrics = aggregate_metrics(results)

    assert metrics["counts"]["PASS"] == 2
    assert metrics["counts"]["FAIL"] == 1
    assert metrics["counts"]["CRASH"] == 0


def test_case_insensitivity_and_unknown():
    results = ["pass", "UNKNOWN_STATUS"]
    metrics = aggregate_metrics(results)

    assert metrics["counts"]["PASS"] == 1
    assert metrics["counts"]["UNKNOWN"] == 1


def test_unique_failures_tracking():
    results = ["FAIL", "FAIL", "CRASH", "CRASH"]
    metrics = aggregate_metrics(results)

    assert metrics["counts"]["FAIL"] == 2
    assert metrics["counts"]["CRASH"] == 2
    assert metrics["unique_failures"] == {"FAIL", "CRASH"}


def test_no_failures():
    results = ["PASS", "TIMEOUT"]
    metrics = aggregate_metrics(results)

    assert metrics["unique_failures"] == set()
