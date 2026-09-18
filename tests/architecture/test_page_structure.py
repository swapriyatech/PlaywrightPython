from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_page_implementations_are_grouped_by_common_page_and_application():
    pages = ROOT / "pages"
    assert (pages / "commonPage" / "CommonPage.py").is_file()
    assert (pages / "app1" / "homepage.py").is_file()
    assert (pages / "app2" / "searchpage.py").is_file()
