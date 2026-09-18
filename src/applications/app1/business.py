from automation.pages.app1.homepage import HomePage
from core.world.scenario_context import ScenarioContext


class CricbuzzNavigationBusiness:
    def __init__(self, context: ScenarioContext) -> None:
        if context.page is None:
            raise RuntimeError("Scenario page is not available")
        self._context = context
        self._page = HomePage(context.page, context.actions())

    def open_home(self) -> str:
        base_url = self._context.manifest.base_urls[self._context.config.environment]
        self._page.open(base_url)
        return self._page.title()
