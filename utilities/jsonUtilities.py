from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class JsonUtilities:
    @staticmethod
    def load(path: Path) -> Any:
        with path.open(encoding="utf-8") as stream:
            return json.load(stream)

    @staticmethod
    def load_object(path: Path) -> dict[str, Any]:
        value = JsonUtilities.load(path)
        if not isinstance(value, dict):
            raise ValueError(f"JSON root must be an object: {path}")
        return value

    @staticmethod
    def save(path: Path, value: Any, indent: int = 2) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, indent=indent, ensure_ascii=False)
            stream.write("\n")

    @staticmethod
    def merge(*objects: dict[str, Any]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for value in objects:
            result.update(value)
        return result

    @staticmethod
    def get_path(value: dict[str, Any], path: str, default: Any = None) -> Any:
        current: Any = value
        for key in path.split("."):
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current

    @staticmethod
    def set_path(value: dict[str, Any], path: str, data: Any) -> None:
        keys = path.split(".")
        current = value
        for key in keys[:-1]:
            child = current.setdefault(key, {})
            if not isinstance(child, dict):
                raise ValueError(f"Cannot assign through non-object path: {path}")
            current = child
        current[keys[-1]] = data
