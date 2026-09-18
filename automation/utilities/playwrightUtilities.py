from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any, TypeVar

from playwright.sync_api import Locator, Page

T = TypeVar("T")


class PlaywrightUtilities:
    @staticmethod
    def wait_visible(locator: Locator, timeout: int) -> None:
        locator.wait_for(state="visible", timeout=timeout)

    @staticmethod
    def wait_hidden(locator: Locator, timeout: int) -> None:
        locator.wait_for(state="hidden", timeout=timeout)

    @staticmethod
    def click(locator: Locator, timeout: int) -> None:
        locator.click(timeout=timeout)

    @staticmethod
    def fill(locator: Locator, value: str, timeout: int) -> None:
        locator.fill(value, timeout=timeout)

    @staticmethod
    def clear(locator: Locator, timeout: int) -> None:
        locator.clear(timeout=timeout)

    @staticmethod
    def press(locator: Locator, key: str, timeout: int) -> None:
        locator.press(key, timeout=timeout)

    @staticmethod
    def select(locator: Locator, value: str, timeout: int) -> None:
        locator.select_option(value, timeout=timeout)

    @staticmethod
    def check(locator: Locator, timeout: int) -> None:
        locator.check(timeout=timeout)

    @staticmethod
    def uncheck(locator: Locator, timeout: int) -> None:
        locator.uncheck(timeout=timeout)

    @staticmethod
    def hover(locator: Locator, timeout: int) -> None:
        locator.hover(timeout=timeout)

    @staticmethod
    def upload(locator: Locator, file_path: Path, timeout: int) -> None:
        locator.set_input_files(str(file_path), timeout=timeout)

    @staticmethod
    def scroll(page: Page, x: int = 0, y: int = 500) -> None:
        page.mouse.wheel(x, y)

    @staticmethod
    def wait_for_url(page: Page, url: str, timeout: int) -> None:
        page.wait_for_url(url, timeout=timeout)

    @staticmethod
    def wait_for_load_state(
        page: Page, state: str = "domcontentloaded", timeout: int = 30_000
    ) -> None:
        page.wait_for_load_state(state=state, timeout=timeout)

    @staticmethod
    def wait_for_response(
        page: Page, predicate: Callable[[object], bool], action: Callable[[], T]
    ) -> T:
        with page.expect_response(predicate):
            return action()

    @staticmethod
    def locator(page: Page, selector: str) -> Locator:
        return page.locator(selector)

    @staticmethod
    def count(locator: Locator) -> int:
        return locator.count()

    @staticmethod
    def is_visible(locator: Locator) -> bool:
        return locator.is_visible()

    @staticmethod
    def is_enabled(locator: Locator) -> bool:
        return locator.is_enabled()

    @staticmethod
    def evaluate(page: Page, expression: str, arg: Any = None) -> Any:
        return page.evaluate(expression, arg)

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
