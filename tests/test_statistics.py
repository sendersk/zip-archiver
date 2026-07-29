from pathlib import Path
from zipfile import ZipFile

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


def test_compression_ratio_calculation() -> None:
    """
    Should calculate compression ratio correctly.
    """

    result = ArchiveStatistics._calculate_compression_ratio(
        original_size=1000,
        archive_size=400,
    )

    assert result == 60.0


def test_saved_space_calculation() -> None:
    """
    Should calculate saved space correctly.
    """

    result = ArchiveStatistics._calculate_saved_space(
        original_size=1000,
        archive_size=400,
    )

    assert result == 600


def test_compression_ratio_with_empty_archive() -> None:
    """
    Should return zero ratio for empty input.
    """

    result = ArchiveStatistics._calculate_compression_ratio(
        original_size=0,
        archive_size=0,
    )

    assert result == 0.0


def test_configuration_snapshot() -> None:
    """
    Should store archive configuration.
    """

    config = ArchiveStatistics._create_configuration(
        recursive=True,
        date_source="modified",
        remove_originals=False,
    )

    assert config.recursive is True
    assert config.date_source == "modified"
    assert config.remove_originals is False
    assert config.compression == "ZIP_DEFLATED"


def test_archive_details_generation(tmp_path: Path) -> None:
    """
    Should generate details for single archive.
    """

    source = tmp_path / "file.txt"
    source.write_text("example data")

    archive = tmp_path / "archive.zip"
    archive.write_text("zip")

    plan = ArchiveEntry(
        year=2025,
        archive_name="archive.zip",
        files=[source],
    )

    details = ArchiveStatistics()._build_archive_details(
        archive,
        plan,
    )

    assert details.year == 2025
    assert details.archive_name == "archive.zip"
    assert details.files == 1
    assert details.original_size > 0
    assert details.archive_size > 0
    assert details.saved_space >= 0


def test_archive_details_are_sorted_by_year(
        tmp_path: Path,
) -> None:
    """
    Should sort archive details by year.
    """

    archive_1 = tmp_path / "2025.zip"
    archive_2 = tmp_path / "2023.zip"

    archive_1.write_text("zip")
    archive_2.write_text("zip")

    file = tmp_path / "file.txt"
    file.write_text("data")

    plans = [
        ArchiveEntry(
            year=2025,
            archive_name="2025.zip",
            files=[file],
        ),
        ArchiveEntry(
            year=2023,
            archive_name="2023.zip",
            files=[file],
        ),
    ]

    report = ArchiveStatistics().create_report(
        [archive_1, archive_2],
        plans,
    )

    assert report.archives[0].year == 2023
    assert report.archives[1].year == 2025