from pathlib import Path

import pytest
from pypdf import PdfWriter

from automation.utilities.csvUtilities import CsvUtilities
from automation.utilities.excelUtilities import ExcelUtilities
from automation.utilities.fileUtilities import FileUtilities
from automation.utilities.jsonUtilities import JsonUtilities
from automation.utilities.pdfUtilities import PdfUtilities
from automation.utilities.pythonUtilities import PythonUtilities
from automation.utilities.yamlUtilities import YamlUtilities


def test_json_yaml_csv_and_file_utilities(tmp_path: Path):
    json_path = tmp_path / "data.json"
    JsonUtilities.save(json_path, {"nested": {"value": 7}})
    data = JsonUtilities.load_object(json_path)
    assert JsonUtilities.get_path(data, "nested.value") == 7
    JsonUtilities.set_path(data, "nested.updated", True)
    assert data["nested"]["updated"] is True

    yaml_path = tmp_path / "data.yaml"
    YamlUtilities.save(yaml_path, {"enabled": True})
    assert YamlUtilities.load_mapping(yaml_path)["enabled"] is True

    csv_path = tmp_path / "data.csv"
    CsvUtilities.write_rows(csv_path, [{"id": "1"}])
    assert CsvUtilities.read_rows(csv_path) == [{"id": "1"}]

    copied = FileUtilities.copy(csv_path, tmp_path / "copy.csv")
    assert copied.is_file()


def test_python_utilities_validate_and_retry(monkeypatch):
    monkeypatch.setenv("UTILITY_TEST_VALUE", "yes")
    assert PythonUtilities.parse_bool(PythonUtilities.required_env("UTILITY_TEST_VALUE"))
    assert PythonUtilities.parse_int("3", minimum=1) == 3
    assert PythonUtilities.retry(lambda: "done") == "done"
    with pytest.raises(ValueError):
        PythonUtilities.parse_bool("unknown")


def test_excel_utilities_round_trip(tmp_path: Path):
    path = tmp_path / "data.xlsx"
    rows = [{"id": 1, "name": "sample"}]
    ExcelUtilities.write_rows(path, "Data", rows)
    assert ExcelUtilities.sheet_names(path) == ["Data"]
    assert ExcelUtilities.read_rows(path, "Data") == rows
    assert ExcelUtilities.read_cell(path, "Data", "B2") == "sample"
    ExcelUtilities.append_rows(path, "Data", [{"id": 2, "name": "second"}])
    assert len(ExcelUtilities.read_rows(path, "Data")) == 2


def test_pdf_utilities_count_extract_merge_and_split(tmp_path: Path):
    source = tmp_path / "source.pdf"
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    writer.add_blank_page(width=200, height=200)
    with source.open("wb") as stream:
        writer.write(stream)
    assert PdfUtilities.page_count(source) == 2
    assert PdfUtilities.extract_text(source) == "\n"
    split_files = PdfUtilities.split(source, tmp_path / "split")
    assert len(split_files) == 2
    merged = tmp_path / "merged.pdf"
    PdfUtilities.merge(merged, split_files)
    assert PdfUtilities.page_count(merged) == 2
