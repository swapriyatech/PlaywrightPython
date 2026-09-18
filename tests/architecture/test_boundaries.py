from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_core_does_not_import_application_modules():
    for path in (ROOT / "src" / "core").rglob("*.py"):
        assert "applications." not in path.read_text(encoding="utf-8")


def test_applications_have_manifests():
    manifests = sorted((ROOT / "src" / "applications").glob("*/manifest.yaml"))
    assert [path.parent.name for path in manifests] == ["app1", "app2"]
