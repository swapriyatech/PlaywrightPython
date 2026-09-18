from __future__ import annotations

import shutil
from pathlib import Path


class FileUtilities:
    @staticmethod
    def ensure_directory(path: Path) -> Path:
        path.mkdir(parents=True, exist_ok=True)
        return path

    @staticmethod
    def copy(source: Path, destination: Path) -> Path:
        destination.parent.mkdir(parents=True, exist_ok=True)
        return Path(shutil.copy2(source, destination))

    @staticmethod
    def move(source: Path, destination: Path) -> Path:
        destination.parent.mkdir(parents=True, exist_ok=True)
        return Path(shutil.move(source, destination))

    @staticmethod
    def remove(path: Path) -> None:
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()

    @staticmethod
    def list_files(directory: Path, pattern: str = "*") -> list[Path]:
        return sorted(path for path in directory.glob(pattern) if path.is_file())

    @staticmethod
    def clean_directory(directory: Path) -> None:
        for path in directory.iterdir():
            FileUtilities.remove(path)
