from playwright.sync_api import Page

from core.actions.base_actions import BaseActions
from locators.app1.CricbuzzHomePageLocators import CricbuzzHomePageLocators
from pages.commonPage.CommonPage import CommonPage


class HomePage(CommonPage):
    def __init__(self, page: Page, actions: BaseActions) -> None:
        super().__init__(page, actions)
        self.locators = CricbuzzHomePageLocators(page)

    def title(self) -> str:
        return self.page.title()
