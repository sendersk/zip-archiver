from pathlib import Path

from zip_archiver.scanner import FileScanner


def test_scan_returns_files(tmp_path: Path) -> None:
    """Should return all files from a directory."""

    (tmp_path / "file1.txt").write_text("data")
    (tmp_path / "file2.txt").write_text("data")

    scanner = FileScanner(tmp_path)

    files = scanner.scan()

    assert len(files) == 2


def test_scan_ignores_directories(tmp_path: Path) -> None:
    """Should ignore nested directories."""

    (tmp_path / "file.txt").write_text("data")
    (tmp_path / "archive").mkdir()

    scanner = FileScanner(tmp_path)

    files = scanner.scan()

    assert len(files) == 1
    assert files[0].name == "file.txt"


def test_recursive_scan_finds_nested_files(tmp_path: Path) -> None:
    """Should find files inside nested directories."""

    nested = tmp_path / "nested"
    nested.mkdir()

    (nested / "file.txt").write_text("data")

    scanner = FileScanner(
        tmp_path,
        recursive=True,
    )

    files = scanner.scan()

    assert len(files) == 1
    assert files[0].name == "file.txt"


def test_non_recursive_scan_ignores_nested_files(tmp_path: Path,) -> None:
    """Should ignore nested files when recursive mode is disabled."""

    nested = tmp_path / "nested"
    nested.mkdir()

    (nested / "file.txt").write_text("data")

    scanner = FileScanner(tmp_path)

    files = scanner.scan()

    assert len(files) == 0