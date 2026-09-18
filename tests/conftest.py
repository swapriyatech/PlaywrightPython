import re
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from core.configuration.models import load_runtime_config
from core.data.repository import TestDataRepository
from core.registry.application_registry import ApplicationRegistry
from core.reporting.evidence import EvidenceCapture
from core.world.scenario_context import ScenarioContext

ROOT = Path(__file__).resolve().parents[1]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    context = item.funcargs.get("scenario_context")
    if context is None or context.page is None:
        return
    scenario_id = re.sub(r"[^a-zA-Z0-9_.-]", "_", item.nodeid)
    EvidenceCapture(ROOT / "reports" / "artifacts").capture_failure(context.page, scenario_id)


@pytest.fixture(scope="session")
def framework_config():
    return load_runtime_config(ROOT / "config" / "framework.yaml")


@pytest.fixture(scope="session")
def application_registry():
    return ApplicationRegistry(ROOT / "src" / "applications")


@pytest.fixture(scope="session")
def data_repository():
    return TestDataRepository(ROOT / "automation" / "testData")


@pytest.fixture(scope="session")
def common_data(data_repository):
    return data_repository.load_common_data()


@pytest.fixture(scope="session")
def all_application_common_data(data_repository):
    return data_repository.load_all_application_common_data()


@pytest.fixture
def data_context(request, data_repository):
    application = next((name for name in ("app1", "app2") if name in request.node.keywords), "app1")
    suite = next(
        (
            name
            for name in ("smoke", "sanity", "regression", "e2e")
            if name in request.node.keywords
        ),
        "smoke",
    )
    test_case = next((name for name in request.node.keywords if name.startswith("TC")), "TC001")
    return application, suite, test_case, data_repository


@pytest.fixture
def application_common_data(data_context):
    application, _, _, data_repository = data_context
    return data_repository.load_application_common(application)


@pytest.fixture
def test_case_data(data_context):
    application, suite, test_case, data_repository = data_context
    return data_repository.merge(
        data_repository.load_suite_data(application, suite),
        data_repository.load_test_case_data(application, suite, test_case),
    )


@pytest.fixture
def test_data(data_context):
    application, suite, test_case, data_repository = data_context
    return data_repository.load_case(application, suite, test_case)


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
