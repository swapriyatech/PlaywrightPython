from __future__ import annotations

import os
import secrets
import time
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import TypeVar

T = TypeVar("T")


class PythonUtilities:
    @staticmethod
    def required_env(name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise RuntimeError(f"Environment variable {name} is required")
        return value

    @staticmethod
    def optional_env(name: str, default: str | None = None) -> str | None:
        return os.getenv(name, default)

    @staticmethod
    def parse_bool(value: str) -> bool:
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "y", "on"}:
            return True
        if normalized in {"0", "false", "no", "n", "off"}:
            return False
        raise ValueError(f"Invalid boolean value: {value!r}")

    @staticmethod
    def parse_int(value: str, minimum: int | None = None, maximum: int | None = None) -> int:
        result = int(value)
        if minimum is not None and result < minimum:
            raise ValueError(f"Value must be >= {minimum}: {result}")
        if maximum is not None and result > maximum:
            raise ValueError(f"Value must be <= {maximum}: {result}")
        return result

    @staticmethod
    def unique_id(prefix: str = "run") -> str:
        return f"{prefix}-{secrets.token_hex(8)}"

    @staticmethod
    def retry(operation: Callable[[], T], attempts: int = 3, delay_seconds: float = 0.5) -> T:
        if attempts < 1:
            raise ValueError("attempts must be at least 1")
        last_error: Exception | None = None
        for attempt in range(attempts):
            try:
                return operation()
            except Exception as error:
                last_error = error
                if attempt < attempts - 1:
                    time.sleep(delay_seconds)
        if last_error is None:
            raise RuntimeError("Retry operation ended without an error")
        raise last_error

    @staticmethod
    def is_blank(value: object) -> bool:
        return value is None or (isinstance(value, str) and not value.strip())

    @staticmethod
    def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
        if minimum > maximum:
            raise ValueError("minimum cannot be greater than maximum")
        return max(minimum, min(value, maximum))

    @staticmethod
    def chunks(values: Iterable[T], size: int) -> list[list[T]]:
        if size < 1:
            raise ValueError("size must be at least 1")
        result: list[list[T]] = []
        chunk: list[T] = []
        for value in values:
            chunk.append(value)
            if len(chunk) == size:
                result.append(chunk)
                chunk = []
        if chunk:
            result.append(chunk)
        return result

    @staticmethod
    def deep_merge(*objects: dict[str, object]) -> dict[str, object]:
        result: dict[str, object] = {}
        for source in objects:
            for key, value in source.items():
                if isinstance(result.get(key), dict) and isinstance(value, dict):
                    result[key] = PythonUtilities.deep_merge(result[key], value)  # type: ignore[arg-type]
                else:
                    result[key] = value
        return result

    @staticmethod
    def safe_filename(value: str, replacement: str = "_") -> str:
        invalid = '<>:"/\\|?*'
        return "".join(
            replacement if character in invalid else character for character in value
        ).strip()

    @staticmethod
    def absolute_path(value: str | Path, base: Path | None = None) -> Path:
        path = Path(value)
        return path if path.is_absolute() else (base or Path.cwd()) / path
