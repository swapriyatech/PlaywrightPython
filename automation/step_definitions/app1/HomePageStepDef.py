import pytest
from pytest_bdd import then

from applications.app1.business import CricbuzzNavigationBusiness


@pytest.fixture
def cricbuzz_business(scenario_context):
    return CricbuzzNavigationBusiness(scenario_context)


@then("the Cricbuzz page has a title")
def cricbuzz_title(scenario_context) -> None:
    assert scenario_context.page is not None
    assert scenario_context.page.title()
