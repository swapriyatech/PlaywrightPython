from __future__ import annotations

from pathlib import Path
from typing import Any

from playwright.sync_api import Locator, Page


class PlaywrightUtilities:
    @staticmethod
    def wait_visible(locator: Locator, timeout: int) -> None:
        locator.wait_for(state="visible", timeout=timeout)

    @staticmethod
    def wait_hidden(locator: Locator, timeout: int) -> None:
        locator.wait_for(state="hidden", timeout=timeout)

    @staticmethod
    def text(locator: Locator, timeout: int) -> str:
        return locator.inner_text(timeout=timeout)

    @staticmethod
    def attribute(locator: Locator, name: str, timeout: int) -> str | None:
        return locator.get_attribute(name, timeout=timeout)

    @staticmethod
    def screenshot(page: Page, output: Path, full_page: bool = True) -> Path:
        output.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(output), full_page=full_page)
        return output

    @staticmethod
    def save_storage_state(context: Any, output: Path) -> Path:
        output.parent.mkdir(parents=True, exist_ok=True)
        context.storage_state(path=str(output))
        return output

    @staticmethod
    def console_messages(page: Page) -> list[str]:
        messages: list[str] = []
        page.on("console", lambda message: messages.append(message.text))
        return messages
