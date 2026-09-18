from __future__ import annotations

import csv
from pathlib import Path


class CsvUtilities:
    @staticmethod
    def read_rows(path: Path) -> list[dict[str, str]]:
        with path.open(newline="", encoding="utf-8") as stream:
            return list(csv.DictReader(stream))

    @staticmethod
    def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
        if not rows:
            raise ValueError("At least one row is required")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
