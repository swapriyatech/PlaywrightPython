from playwright.sync_api import Locator, Page


class GoogleSearchPageLocators:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_box: Locator = page.get_by_role("combobox", name="Search")
        self.results: Locator = page.get_by_role("heading", level=3).first
