from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUITES = {"smoke", "sanity", "regression", "e2e"}


def test_each_application_has_all_feature_suites():
    for application in ("app1", "app2"):
        directories = {
            path.name for path in (ROOT / "features" / application).iterdir() if path.is_dir()
        }
        assert directories == SUITES
