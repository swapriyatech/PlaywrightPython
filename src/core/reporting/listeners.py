from __future__ import annotations

from core.events.contracts import Event
from core.reporting.email import EmailReporter
from core.reporting.history import ExecutionHistory, ExecutionSummary


class ExecutionHistoryListener:
    def __init__(self, history: ExecutionHistory) -> None:
        self._history = history

    def handle(self, event: Event) -> None:
        if event.name != "ExecutionComplete":
            return
        metadata = event.metadata
        summary = ExecutionSummary(
            execution_id=event.execution_id,
            application=metadata["application"],
            environment=metadata["environment"],
            browser=metadata["browser"],
            suite=metadata["suite"],
            total=int(metadata["total"]),
            passed=int(metadata["passed"]),
            failed=int(metadata["failed"]),
            skipped=int(metadata["skipped"]),
            duration_seconds=float(metadata["duration_seconds"]),
        )
        self._history.record(summary)


class ExecutionEmailListener:
    def __init__(self, reporter: EmailReporter) -> None:
        self._reporter = reporter

    def handle(self, event: Event) -> None:
        if event.name != "ExecutionComplete":
            return
        metadata = event.metadata
        subject = f"Automation execution {event.execution_id}: {metadata['failed']} failed"
        body = "\n".join(f"{key}: {value}" for key, value in sorted(metadata.items()))
        self._reporter.send(subject, body)
