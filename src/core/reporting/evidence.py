from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Page


class EvidenceCapture:
    def __init__(self, output_dir: Path) -> None:
        self._output_dir = output_dir

    def capture_failure(self, page: Page, scenario_id: str) -> Path:
        self._output_dir.mkdir(parents=True, exist_ok=True)
        destination = self._output_dir / f"{scenario_id}-failure.png"
        page.screenshot(path=str(destination), full_page=True)
        return destination
