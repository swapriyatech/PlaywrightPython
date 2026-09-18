import pytest
from pytest_bdd import given, then, when

from applications.app1.business import CricbuzzNavigationBusiness


@pytest.fixture
def cricbuzz_business(scenario_context):
    return CricbuzzNavigationBusiness(scenario_context)


@given("I open the app1 application")
def open_app1(cricbuzz_business: CricbuzzNavigationBusiness) -> None:
    cricbuzz_business.open_home()


@when("I open the Cricbuzz home page")
def open_cricbuzz(cricbuzz_business: CricbuzzNavigationBusiness) -> None:
    cricbuzz_business.open_home()


@then("the Cricbuzz page has a title")
def cricbuzz_title(scenario_context) -> None:
    assert scenario_context.page is not None
    assert scenario_context.page.title()
