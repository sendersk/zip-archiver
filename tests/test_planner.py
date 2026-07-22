from datetime import datetime
from pathlib import Path

from zip_archiver.date_resolver import FileDateResolver
from zip_archiver.planner import ArchivePlanner


def test_group_files_by_year(tmp_path: Path) -> None:
    """Should group files by year."""

    file1 = tmp_path / "invoice_2024.pdf"
    file2 = tmp_path / "photo_2024.jpg"
    file3 = tmp_path / "backup_2025.zip"

    file1.touch()
    file2.touch()
    file3.touch()

    planner = ArchivePlanner(
        FileDateResolver(),
        date_source="filename",
    )

    plan = planner.create_plan(
        tmp_path,
        [file1, file2, file3]
    )

    assert len(plan) == 2
    assert plan[0].year == 2024
    assert len(plan[0].files) == 2
    assert plan[1].year == 2025

def test_skip_current_year(tmp_path: Path) -> None:
    """Should not archive current-year files."""

    current = datetime.now().year

    file = tmp_path / f"invoice_{current}.pdf"
    file.touch()

    planner = ArchivePlanner(
        FileDateResolver(),
        date_source="filename",
    )

    plan = planner.create_plan(tmp_path, [file],)

    assert plan == []