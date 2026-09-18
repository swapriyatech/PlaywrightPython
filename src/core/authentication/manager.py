from __future__ import annotations

from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Protocol

from playwright.sync_api import BrowserContext


class AuthenticationProvider(Protocol):
    def authenticate(self, context: BrowserContext) -> None: ...


class AuthenticationManager:
    def __init__(self, state_dir: Path, validity: timedelta = timedelta(hours=8)) -> None:
        self._state_dir = state_dir
        self._validity = validity

    def state_path(self, application: str, environment: str, user: str) -> Path:
        safe_user = user.replace("/", "_").replace("\\", "_")
        return self._state_dir / f"{application}-{environment}-{safe_user}.storage.json"

    def is_valid(self, path: Path) -> bool:
        if not path.is_file():
            return False
        age = datetime.now(UTC) - datetime.fromtimestamp(path.stat().st_mtime, UTC)
        return age < self._validity

    def ensure_state(
        self,
        context: BrowserContext,
        application: str,
        environment: str,
        user: str,
        provider: AuthenticationProvider,
    ) -> Path:
        path = self.state_path(application, environment, user)
        if not self.is_valid(path):
            self._state_dir.mkdir(parents=True, exist_ok=True)
            provider.authenticate(context)
            context.storage_state(path=str(path))
        return path
