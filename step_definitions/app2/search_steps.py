import pytest
from pytest_bdd import given, parsers, then, when

from applications.app2.business import GoogleSearchBusiness


@pytest.fixture
def google_business(scenario_context):
    return GoogleSearchBusiness(scenario_context)


@given("I open the app2 application")
def open_app2(google_business: GoogleSearchBusiness) -> None:
    google_business.open_application()


@when(parsers.parse('I search Google for "{query}"'))
def search_google(google_business: GoogleSearchBusiness, query: str) -> None:
    google_business.search(query)


@then("Google returns search results")
def google_results(scenario_context) -> None:
    assert scenario_context.page is not None
    assert "/search" in scenario_context.page.url
    assert "/sorry" not in scenario_context.page.url
