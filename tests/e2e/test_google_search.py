import os

import pytest
from pytest_bdd import scenarios

pytest_plugins = [
    "automation.step_definitions.common.BrowserStepDef",
    "automation.step_definitions.common.ApplicationStepDef",
    "automation.step_definitions.common.data_steps",
    "automation.step_definitions.app2.SearchPageStepDef",
]

pytestmark = [
    pytest.mark.app2,
    pytest.mark.skipif(
        os.getenv("RUN_BROWSER_TESTS", "false").lower() != "true",
        reason="Set RUN_BROWSER_TESTS=true for external-site E2E scenarios",
    ),
]

scenarios(
    "../../automation/features/app2/smoke/google_search.feature",
    "../../automation/features/app2/sanity/google_search.feature",
    "../../automation/features/app2/regression/google_search.feature",
    "../../automation/features/app2/e2e/google_search.feature",
)
