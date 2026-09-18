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
        sources = [self._load_optional(self._root / "common" / "commonData.json")]
        app_root = self._root / application
        sources.append(self._load_optional(app_root / "appCommon.json"))
        sources.append(self._load_optional(app_root / suite / "suiteData.json"))
        if test_case:
            sources.append(self._load_optional(app_root / suite / f"{test_case}.json"))
        if runtime_override:
            sources.append(runtime_override)
        return self._engine.merge(*sources)

    def _load_optional(self, path: Path) -> dict[str, Any]:
        return self._engine.load_json(path) if path.is_file() else {}
