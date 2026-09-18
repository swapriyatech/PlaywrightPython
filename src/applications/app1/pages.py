from playwright.sync_api import Page

from applications.app1.locators import CricbuzzHomeLocators
from core.actions.base_actions import BaseActions


class CricbuzzHomePage:
    def __init__(self, page: Page, actions: BaseActions) -> None:
        self._page = page
        self._actions = actions
        self.locators = CricbuzzHomeLocators(page)

    def open(self, base_url: str) -> None:
        self._page.goto(base_url, wait_until="domcontentloaded")

    def title(self) -> str:
        return self._page.title()
