from __future__ import annotations

from typing import Protocol

from core.events.contracts import Event


class Plugin(Protocol):
    name: str

    def handle(self, event: Event) -> None: ...


class PluginManager:
    def __init__(self, plugins: tuple[Plugin, ...] = ()) -> None:
        names = [plugin.name for plugin in plugins]
        if len(names) != len(set(names)):
            raise ValueError("Plugin names must be unique")
        self._plugins = plugins

    def dispatch(self, event: Event) -> None:
        for plugin in self._plugins:
            plugin.handle(event)
