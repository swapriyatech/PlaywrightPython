import os

import pytest
from pytest_bdd import scenarios

pytest_plugins = [
    "step_definitions.common.BrowserStepDef",
    "step_definitions.common.ApplicationStepDef",
    "step_definitions.common.data_steps",
    "step_definitions.app1.HomePageStepDef",
]

pytestmark = [
    pytest.mark.app1,
    pytest.mark.skipif(
        os.getenv("RUN_BROWSER_TESTS", "false").lower() != "true",
        reason="Set RUN_BROWSER_TESTS=true for external-site E2E scenarios",
    ),
]

scenarios(
    "../../features/app1/smoke/cricbuzz_home.feature",
    "../../features/app1/sanity/cricbuzz_home.feature",
    "../../features/app1/regression/cricbuzz_home.feature",
    "../../features/app1/e2e/cricbuzz_home.feature",
)
