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