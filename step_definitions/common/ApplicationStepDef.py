from pytest_bdd import given, parsers


@given(parsers.parse("I open the {application} application"))
def open_application(scenario_context, application: str) -> None:
    if scenario_context.manifest.name != application:
        raise ValueError(
            f"Scenario application {application!r} does not match "
            f"manifest {scenario_context.manifest.name!r}"
        )
    if scenario_context.page is None:
        raise RuntimeError("Browser page was not created for the scenario")
    base_url = scenario_context.manifest.base_urls[scenario_context.config.environment]
    scenario_context.page.goto(base_url, wait_until="domcontentloaded")
