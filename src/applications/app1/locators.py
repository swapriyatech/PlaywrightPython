from playwright.sync_api import Locator, Page


class CricbuzzHomeLocators:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def headline(self) -> Locator:
        return self.page.locator("h1").first
