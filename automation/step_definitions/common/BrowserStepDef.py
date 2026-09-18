from pytest_bdd import given


@given("I launch the browser")
def launch_browser(scenario_context) -> None:
    if scenario_context.page is None:
        raise RuntimeError("Browser page was not created for the scenario")
