import os

import pytest
from pytest_bdd import scenarios

pytest_plugins = [
    "automation.step_definitions.common.BrowserStepDef",
    "automation.step_definitions.common.ApplicationStepDef",
    "automation.step_definitions.common.data_steps",
    "automation.step_definitions.app1.HomePageStepDef",
]

pytestmark = [
    pytest.mark.app1,
    pytest.mark.skipif(
        os.getenv("RUN_BROWSER_TESTS", "false").lower() != "true",
        reason="Set RUN_BROWSER_TESTS=true for external-site E2E scenarios",
    ),
]

scenarios(
    "../../automation/features/app1/smoke/cricbuzz_home.feature",
    "../../automation/features/app1/sanity/cricbuzz_home.feature",
    "../../automation/features/app1/regression/cricbuzz_home.feature",
    "../../automation/features/app1/e2e/cricbuzz_home.feature",
)
