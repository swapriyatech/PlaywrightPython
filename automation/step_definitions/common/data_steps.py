from pytest_bdd import given, parsers


@given("I load common data")
def load_common_data(common_data: dict[str, object]) -> None:
    if "locale" not in common_data:
        raise AssertionError("Common data must contain locale")


@given("I load all application common data")
def load_all_application_common_data(
    all_application_common_data: dict[str, dict[str, object]],
) -> None:
    if not {"app1", "app2"}.issubset(all_application_common_data):
        raise AssertionError("Common data for app1 and app2 is required")


@given(parsers.parse("I load common data for {application} application"))
def load_application_common_data(
    application_common_data: dict[str, object], application: str
) -> None:
    if application_common_data.get("application") != application:
        raise AssertionError(f"Application common data does not match {application}")


@given(parsers.parse('I load {application} test case data "{test_case}"'))
def load_application_test_data(
    test_case_data: dict[str, object], application: str, test_case: str
) -> None:
    if test_case_data.get("testCaseId") != test_case:
        raise AssertionError(f"Test case data does not match {test_case}")
    if test_case != "TC001":
        raise AssertionError(f"Unsupported test case: {test_case}")
