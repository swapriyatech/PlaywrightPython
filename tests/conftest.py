from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from core.configuration.models import load_runtime_config
from core.registry.application_registry import ApplicationRegistry
from core.world.scenario_context import ScenarioContext

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def framework_config():
    return load_runtime_config(ROOT / "config" / "framework.yaml")


@pytest.fixture(scope="session")
def application_registry():
    return ApplicationRegistry(ROOT / "src" / "applications")


@pytest.fixture
def scenario_context(request, framework_config, application_registry, tmp_path):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, framework_config.browser)
        browser = browser_type.launch(headless=True)
        application = next(
            (name for name in application_registry.names() if name in request.node.keywords),
            framework_config.application,
        )
        context = ScenarioContext(
            config=framework_config,
            manifest=application_registry.get(application),
            browser=browser,
            artifact_dir=tmp_path,
        )
        context.start()
        try:
            yield context
        finally:
            context.close()
            browser.close()
