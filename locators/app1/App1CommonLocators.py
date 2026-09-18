from playwright.sync_api import Locator, Page


class App1CommonLocators:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def page_body(self) -> Locator:
        return self.page.locator("body")

    @property
    def site_header(self) -> Locator:
        return self.page.locator("header").first
