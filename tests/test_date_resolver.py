from pathlib import Path

from zip_archiver.date_resolver import FileDateResolver


def test_get_modified_year(tmp_path: Path) -> None:
    """Should return the modification year."""

    file = tmp_path / "example.txt"
    file.write_text("data")

    resolver = FileDateResolver()

    year = resolver.get_modified_year(file)

    assert isinstance(year, int)
    assert year >= 2024

def test_extract_year_from_filename() -> None:
    """Should detect year in filename."""

    resolver = FileDateResolver()

    file = Path("invoice_2025.pdf")

    assert resolver.get_filename_year(file) == 2025

def test_return_none_when_filename_has_no_year() -> None:
    """Should return None when filename contains no year."""

    resolver = FileDateResolver()

    file = Path("invoice.pdf")

    assert resolver.get_filename_year(file) is None