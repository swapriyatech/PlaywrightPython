import pytest
from pytest_bdd import parsers, then, when

from applications.app2.business import GoogleSearchBusiness


@pytest.fixture
def google_business(scenario_context):
    return GoogleSearchBusiness(scenario_context)


@when(parsers.parse('I search Google for "{query}"'))
def search_google(google_business: GoogleSearchBusiness, query: str) -> None:
    google_business.search(query)


@then("Google returns search results")
def google_results(scenario_context) -> None:
    if scenario_context.page is None:
        raise AssertionError("Scenario page was not created")
    if "/search" not in scenario_context.page.url:
        raise AssertionError(f"Google search URL was not reached: {scenario_context.page.url}")
    if "/sorry" in scenario_context.page.url:
        raise AssertionError("Google returned an anti-bot challenge page")
