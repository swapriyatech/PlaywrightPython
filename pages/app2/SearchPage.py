from playwright.sync_api import Page

from core.actions.base_actions import BaseActions
from locators.app2.GoogleSearchPageLocators import GoogleSearchPageLocators
from pages.commonPage.CommonPage import CommonPage


class SearchPage(CommonPage):
    def __init__(self, page: Page, actions: BaseActions) -> None:
        super().__init__(page, actions)
        self.locators = GoogleSearchPageLocators(page)

    def search(self, base_url: str, query: str) -> None:
        self.open(base_url)
        self.actions.fill(self.locators.search_box, query)
        self.actions.press(self.locators.search_box, "Enter")

    def has_results(self) -> bool:
        return "/search" in self.page.url and "/sorry" not in self.page.url
