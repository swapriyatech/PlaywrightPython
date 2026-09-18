from playwright.sync_api import Locator, Page


class App1CommonLocators:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_body: Locator = page.locator("body")
        self.site_header: Locator = page.locator("header").first
