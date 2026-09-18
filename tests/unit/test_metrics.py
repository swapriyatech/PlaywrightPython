from core.observability.metrics import ExecutionMetrics


def test_metrics_are_safe_for_empty_and_completed_runs():
    metrics = ExecutionMetrics(total=4, passed=3, failed=1)
    assert metrics.pass_rate == 0.75
    assert metrics.failure_rate == 0.25
    assert ExecutionMetrics().pass_rate == 0.0
