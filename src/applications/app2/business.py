from core.world.scenario_context import ScenarioContext
from pages.app2.SearchPage import SearchPage


class GoogleSearchBusiness:
    def __init__(self, context: ScenarioContext) -> None:
        if context.page is None:
            raise RuntimeError("Scenario page is not available")
        self._context = context
        self._page = SearchPage(context.page, context.actions())

    def search(self, query: str) -> bool:
        base_url = self._context.manifest.base_urls[self._context.config.environment]
        self._page.search(base_url, query)
        return self._page.has_results()

    def open_application(self) -> None:
        base_url = self._context.manifest.base_urls[self._context.config.environment]
        self._page.open(base_url)
