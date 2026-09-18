from playwright.sync_api import Locator, Page


class App2CommonLocators:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_body: Locator = page.locator("body")
        self.site_footer: Locator = page.locator("footer").first
