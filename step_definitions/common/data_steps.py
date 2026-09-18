from pytest_bdd import given, parsers


@given("I load common data")
def load_common_data(test_data: dict[str, object]) -> None:
    assert "locale" in test_data


@given(parsers.parse('I load {application} test case data "{test_case}"'))
def load_application_test_data(
    test_data: dict[str, object], application: str, test_case: str
) -> None:
    assert test_data["application"] == application
    assert test_case == "TC001"
