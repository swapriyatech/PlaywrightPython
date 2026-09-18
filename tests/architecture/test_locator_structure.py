from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APPLICATIONS = ("app1", "app2")
SUITES = ("smoke", "sanity", "regression", "e2e")


def test_locators_are_grouped_by_application_and_page():
    locator_root = ROOT / "automation" / "locators"
    assert (locator_root / "app1" / "App1CommonLocators.py").is_file()
    assert (locator_root / "app1" / "CricbuzzHomePageLocators.py").is_file()
    assert (locator_root / "app2" / "App2CommonLocators.py").is_file()
    assert (locator_root / "app2" / "GoogleSearchPageLocators.py").is_file()


def test_top_level_test_artifacts_have_application_boundaries():
    assert (ROOT / "automation").is_dir()
    assert (ROOT / "automation" / "locators").is_dir()
    assert (ROOT / "automation" / "step_definitions").is_dir()
    assert (ROOT / "automation" / "testData").is_dir()
    assert (ROOT / "automation" / "features").is_dir()
    assert (ROOT / "automation" / "step_definitions" / "common" / "data_steps.py").is_file()
    for application in APPLICATIONS:
        assert (ROOT / "automation" / "locators" / application).is_dir()
        assert (ROOT / "automation" / "step_definitions" / application).is_dir()
        assert (ROOT / "automation" / "testData" / application).is_dir()
        assert {
            path.name for path in (ROOT / "automation" / "features" / application).iterdir()
        } == set(SUITES)
