from playwright.sync_api import Locator, Page


class CricbuzzHomePageLocators:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.headline: Locator = page.locator("h1").first
