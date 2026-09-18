from playwright.sync_api import Page

from applications.app2.locators import GoogleSearchLocators
from core.actions.base_actions import BaseActions


class GoogleSearchPage:
    def __init__(self, page: Page, actions: BaseActions) -> None:
        self._page = page
        self._actions = actions
        self.locators = GoogleSearchLocators(page)

    def search(self, base_url: str, query: str) -> None:
        self._page.goto(base_url, wait_until="domcontentloaded")
        self._actions.fill(self.locators.search_box, query)
        self._actions.press(self.locators.search_box, "Enter")

    def has_results(self) -> bool:
        return "/search" in self._page.url and "/sorry" not in self._page.url
