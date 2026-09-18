from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class ApplicationManifest:
    name: str
    display_name: str
    base_urls: dict[str, str]
    page_module: str
    business_module: str


class ApplicationRegistry:
    def __init__(self, applications_path: Path) -> None:
        self._applications_path = applications_path
        self._manifests = self._discover()

    def _discover(self) -> dict[str, ApplicationManifest]:
        manifests: dict[str, ApplicationManifest] = {}
        for path in sorted(self._applications_path.glob("*/manifest.yaml")):
            with path.open(encoding="utf-8") as stream:
                raw = yaml.safe_load(stream) or {}
            if not isinstance(raw, dict):
                raise ValueError(f"Manifest root must be a mapping: {path}")
            name = raw.get("name")
            if not isinstance(name, str) or not name:
                raise ValueError(f"Manifest name is required: {path}")
            if name in manifests:
                raise ValueError(f"Duplicate application manifest: {name}")
            manifests[name] = ApplicationManifest(
                name=name,
                display_name=str(raw.get("display_name", name)),
                base_urls=dict(raw.get("base_urls", {})),
                page_module=str(raw.get("page_module", "")),
                business_module=str(raw.get("business_module", "")),
            )
        return manifests

    def get(self, name: str) -> ApplicationManifest:
        try:
            return self._manifests[name]
        except KeyError as error:
            available = ", ".join(sorted(self._manifests)) or "none"
            raise ValueError(f"Unknown application {name!r}; available: {available}") from error

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._manifests))
