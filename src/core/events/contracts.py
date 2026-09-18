from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Protocol


@dataclass(frozen=True)
class Event:
    name: str
    execution_id: str
    occurred_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    metadata: dict[str, str] = field(default_factory=dict)


class EventListener(Protocol):
    def handle(self, event: Event) -> None: ...


class EventBus:
    def __init__(self, listeners: tuple[EventListener, ...] = ()) -> None:
        self._listeners = listeners

    def publish(self, event: Event) -> None:
        for listener in self._listeners:
            listener.handle(event)
