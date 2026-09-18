import pytest
from pytest_bdd import then

from applications.app1.business import CricbuzzNavigationBusiness


@pytest.fixture
def cricbuzz_business(scenario_context):
    return CricbuzzNavigationBusiness(scenario_context)


@then("the Cricbuzz page has a title")
def cricbuzz_title(scenario_context) -> None:
    if scenario_context.page is None:
        raise AssertionError("Scenario page was not created")
    if not scenario_context.page.title():
        raise AssertionError("Cricbuzz page title is empty")
