from playwright.sync_api import Locator, Page


class GoogleSearchPageLocators:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def search_box(self) -> Locator:
        return self.page.get_by_role("combobox", name="Search")

    @property
    def results(self) -> Locator:
        return self.page.get_by_role("heading", level=3).first
