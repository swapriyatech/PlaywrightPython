from core.events.contracts import Event, EventBus
from core.reporting.history import ExecutionHistory
from core.reporting.listeners import ExecutionHistoryListener


def test_execution_complete_event_is_persisted(tmp_path):
    history = ExecutionHistory(tmp_path / "history.sqlite3")
    listener = ExecutionHistoryListener(history)
    event = Event(
        "ExecutionComplete",
        "exec-2",
        metadata={
            "application": "app1",
            "environment": "UAT",
            "browser": "chromium",
            "suite": "smoke",
            "total": "2",
            "passed": "2",
            "failed": "0",
            "skipped": "0",
            "duration_seconds": "1.2",
        },
    )
    EventBus((listener,)).publish(event)
    assert history.latest(1)[0].execution_id == "exec-2"
