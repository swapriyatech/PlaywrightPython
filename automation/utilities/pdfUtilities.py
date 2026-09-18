from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader, PdfWriter


class PdfUtilities:
    @staticmethod
    def page_count(path: Path) -> int:
        return len(PdfReader(str(path)).pages)

    @staticmethod
    def extract_text(path: Path, page_number: int | None = None) -> str:
        pages = PdfReader(str(path)).pages
        selected = pages if page_number is None else [pages[page_number]]
        return "\n".join(page.extract_text() or "" for page in selected)

    @staticmethod
    def merge(output: Path, inputs: list[Path]) -> None:
        if not inputs:
            raise ValueError("At least one PDF input is required")
        writer = PdfWriter()
        for path in inputs:
            for page in PdfReader(str(path)).pages:
                writer.add_page(page)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("wb") as stream:
            writer.write(stream)

    @staticmethod
    def split(path: Path, output_dir: Path) -> list[Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        outputs: list[Path] = []
        for index, page in enumerate(PdfReader(str(path)).pages, start=1):
            output = output_dir / f"{path.stem}-page-{index}.pdf"
            writer = PdfWriter()
            writer.add_page(page)
            with output.open("wb") as stream:
                writer.write(stream)
            outputs.append(output)
        return outputs
