from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import Browser, BrowserContext, Page

from core.actions.base_actions import BaseActions
from core.configuration.models import FrameworkConfig
from core.registry.application_registry import ApplicationManifest


@dataclass
class ScenarioContext:
    config: FrameworkConfig
    manifest: ApplicationManifest
    browser: Browser
    artifact_dir: Path
    browser_context: BrowserContext | None = None
    page: Page | None = None

    def start(self) -> None:
        self.browser_context = self.browser.new_context(
            viewport={"width": 1440, "height": 900},
            accept_downloads=True,
            record_video_dir=str(self.artifact_dir / "videos"),
        )
        self.page = self.browser_context.new_page()

    def actions(self) -> BaseActions:
        if self.page is None:
            raise RuntimeError("Scenario has not started")
        return BaseActions(self.page, self.config.timeouts.action)

    def close(self) -> None:
        if self.browser_context is not None:
            self.browser_context.close()
            self.browser_context = None
            self.page = None
