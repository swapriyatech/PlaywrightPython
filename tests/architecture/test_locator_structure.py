from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APPLICATIONS = ("app1", "app2")
SUITES = ("smoke", "sanity", "regression", "e2e")


def test_locators_are_grouped_by_application_and_page():
    locator_root = ROOT / "locators"
    assert (locator_root / "app1" / "CricbuzzHomePageLocators.py").is_file()
    assert (locator_root / "app2" / "GoogleSearchPageLocators.py").is_file()


def test_top_level_test_artifacts_have_application_boundaries():
    assert (ROOT / "locators").is_dir()
    assert (ROOT / "step_definitions").is_dir()
    assert (ROOT / "testData").is_dir()
    assert (ROOT / "features").is_dir()
    for application in APPLICATIONS:
        assert (ROOT / "locators" / application).is_dir()
        assert (ROOT / "step_definitions" / application).is_dir()
        assert (ROOT / "testData" / application).is_dir()
        assert {path.name for path in (ROOT / "features" / application).iterdir()} == set(SUITES)
