from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

from playwright.sync_api import Locator, Page

T = TypeVar("T")


class BaseActions:
    def __init__(self, page: Page, action_timeout: int) -> None:
        self._page = page
        self._action_timeout = action_timeout

    def click(self, locator: Locator) -> None:
        locator.click(timeout=self._action_timeout)

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value, timeout=self._action_timeout)

    def press(self, locator: Locator, key: str) -> None:
        locator.press(key, timeout=self._action_timeout)

    def select(self, locator: Locator, value: str) -> None:
        locator.select_option(value, timeout=self._action_timeout)

    def check(self, locator: Locator) -> None:
        locator.check(timeout=self._action_timeout)

    def uncheck(self, locator: Locator) -> None:
        locator.uncheck(timeout=self._action_timeout)

    def hover(self, locator: Locator) -> None:
        locator.hover(timeout=self._action_timeout)

    def wait_for_response(self, predicate: Callable[[object], bool], action: Callable[[], T]) -> T:
        with self._page.expect_response(predicate):
            return action()
