from pathlib import Path

from core.events.contracts import Event, EventBus
from core.plugins.manager import PluginManager
from core.reporting.history import ExecutionHistory, ExecutionSummary


class Listener:
    def __init__(self) -> None:
        self.events: list[str] = []

    def handle(self, event: Event) -> None:
        self.events.append(event.name)


class NamedPlugin(Listener):
    name = "test-plugin"


def test_event_bus_and_plugin_manager_dispatch_typed_event():
    listener = NamedPlugin()
    event = Event("ExecutionComplete", "exec-1")
    EventBus((listener,)).publish(event)
    PluginManager((listener,)).dispatch(event)
    assert listener.events == ["ExecutionComplete", "ExecutionComplete"]


def test_execution_history_round_trip(tmp_path: Path):
    history = ExecutionHistory(tmp_path / "history.sqlite3")
    summary = ExecutionSummary("exec-1", "app1", "UAT", "chromium", "smoke", 1, 1, 0, 0, 2.5)
    history.record(summary)
    assert history.latest(1) == [summary]
