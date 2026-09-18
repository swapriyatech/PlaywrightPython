from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from core.data.data_engine import TestDataEngine


class TestDataRepository:
    __test__ = False

    _safe_name = re.compile(r"^[a-zA-Z0-9_-]+$")

    def __init__(self, root: Path, engine: TestDataEngine | None = None) -> None:
        self._root = root
        self._engine = engine or TestDataEngine()
        self._cache: dict[Path, dict[str, Any]] = {}

    def load_case(
        self,
        application: str,
        suite: str,
        test_case: str | None = None,
        runtime_override: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        for value in (application, suite, test_case):
            if value is not None and not self._safe_name.fullmatch(value):
                raise ValueError(f"Unsafe test data path component: {value!r}")
        sources = [self.load_common_data(), self.load_application_common(application)]
        sources.append(self.load_suite_data(application, suite))
        if test_case:
            sources.append(self.load_test_case_data(application, suite, test_case))
        if runtime_override:
            sources.append(runtime_override)
        return self._engine.merge(*sources)

    def load_common_data(self) -> dict[str, Any]:
        return self._load_optional(self._root / "common" / "commonData.json")

    def load_all_application_common_data(self) -> dict[str, dict[str, Any]]:
        return {
            application.name: self.load_application_common(application.name)
            for application in self._root.iterdir()
            if application.is_dir() and application.name != "common"
        }

    def load_application_common(self, application: str) -> dict[str, Any]:
        return self._load_optional(self._root / application / "appCommon.json")

    def load_suite_data(self, application: str, suite: str) -> dict[str, Any]:
        return self._load_optional(self._root / application / suite / "suiteData.json")

    def load_test_case_data(self, application: str, suite: str, test_case: str) -> dict[str, Any]:
        return self._load_optional(self._root / application / suite / f"{test_case}.json")

    def merge(self, *sources: dict[str, Any]) -> dict[str, Any]:
        return self._engine.merge(*sources)

    def _load_optional(self, path: Path) -> dict[str, Any]:
        if path not in self._cache:
            self._cache[path] = self._engine.load_json(path) if path.is_file() else {}
        return dict(self._cache[path])
