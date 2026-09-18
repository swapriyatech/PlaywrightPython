from pytest_bdd import given, parsers


@given("I load common data")
def load_common_data(common_data: dict[str, object]) -> None:
    assert "locale" in common_data


@given("I load all application common data")
def load_all_application_common_data(
    all_application_common_data: dict[str, dict[str, object]],
) -> None:
    assert {"app1", "app2"}.issubset(all_application_common_data)


@given(parsers.parse("I load common data for {application} application"))
def load_application_common_data(
    application_common_data: dict[str, object], application: str
) -> None:
    assert application_common_data["application"] == application


@given(parsers.parse('I load {application} test case data "{test_case}"'))
def load_application_test_data(
    test_case_data: dict[str, object], application: str, test_case: str
) -> None:
    assert test_case_data["testCaseId"] == test_case
    assert test_case == "TC001"
