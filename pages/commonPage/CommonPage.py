from playwright.sync_api import Page

from core.actions.base_actions import BaseActions


class CommonPage:
    def __init__(self, page: Page, actions: BaseActions) -> None:
        self.page = page
        self.actions = actions

    def open(self, base_url: str) -> None:
        self.page.goto(base_url, wait_until="domcontentloaded")
