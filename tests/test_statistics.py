from pathlib import Path

from zip_archiver.models import ArchiveEntry
from zip_archiver.statistics import ArchiveStatistics


def test_statistics_report(tmp_path: Path) -> None:
    """Should calculate archive statistics."""

    file = tmp_path / "document.txt"
    file.write_text("Hello")

    archive = tmp_path / "archive.zip"
    archive.write_text("zip")

    plan = ArchiveEntry(
        year=2025,
        archive_name="archive.zip",
        files=[file],
    )

    report = ArchiveStatistics().create_report(
        [archive],
        [plan],
    )

    assert report.archives_created == 1
    assert report.files_archived == 1