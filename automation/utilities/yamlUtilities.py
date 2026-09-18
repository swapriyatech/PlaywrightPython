from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class YamlUtilities:
    @staticmethod
    def load(path: Path) -> Any:
        with path.open(encoding="utf-8") as stream:
            return yaml.safe_load(stream)

    @staticmethod
    def load_mapping(path: Path) -> dict[str, Any]:
        value = YamlUtilities.load(path)
        if not isinstance(value, dict):
            raise ValueError(f"YAML root must be a mapping: {path}")
        return value

    @staticmethod
    def save(path: Path, value: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="\n") as stream:
            yaml.safe_dump(value, stream, sort_keys=False)
