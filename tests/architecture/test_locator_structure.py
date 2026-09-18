from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_locators_are_grouped_by_application_and_page():
    locator_root = ROOT / "locators"
    assert (locator_root / "app1" / "CricbuzzHomePageLocators.py").is_file()
    assert (locator_root / "app2" / "GoogleSearchPageLocators.py").is_file()
