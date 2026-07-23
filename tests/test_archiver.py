from pathlib import Path
from zipfile import ZipFile

from zip_archiver.archiver import ZipArchiver
from zip_archiver.models import ArchiveEntry


def test_create_archive(tmp_path: Path) -> None:
    """Should create a ZIP archive."""

    file = tmp_path / "document.txt"
    file.write_text("Hello")

    plan = ArchiveEntry(
        year=2025,
        archive_name="archive.zip",
        files=[file],
    )

    archiver = ZipArchiver()

    archive = archiver.create_archive(tmp_path, plan,)

    assert archive.exists()

    with ZipFile(archive) as zip_file:
        assert "document.txt" in zip_file.namelist()

def test_verify_archive(tmp_path: Path) -> None:
    """Should verify a valid archive."""

    file = tmp_path / "file.txt"
    file.write_text("data")

    plan = ArchiveEntry(
        year=2025,
        archive_name="archive.zip",
        files=[file],
    )

    archiver = ZipArchiver()

    archive = archiver.create_archive(
        tmp_path,
        plan,
    )

    assert archiver.verify_archive(archive)