import os

import pytest
from pytest_bdd import scenarios

pytest_plugins = ["step_definitions.app2.search_steps"]

pytestmark = [
    pytest.mark.app2,
    pytest.mark.skipif(
        os.getenv("RUN_BROWSER_TESTS", "false").lower() != "true",
        reason="Set RUN_BROWSER_TESTS=true for external-site E2E scenarios",
    ),
]

scenarios("../../features/app2/smoke/google_search.feature")
