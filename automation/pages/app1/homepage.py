from playwright.sync_api import Page

from automation.locators.app1.CricbuzzHomePageLocators import CricbuzzHomePageLocators
from automation.pages.commonPage.CommonPage import CommonPage
from core.actions.base_actions import BaseActions


class HomePage(CommonPage):
    def __init__(self, page: Page, actions: BaseActions) -> None:
        super().__init__(page, actions)
        self.locators = CricbuzzHomePageLocators(page)

    def title(self) -> str:
        return self.page.title()
