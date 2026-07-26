import json

from zip_archiver.models import ArchiveReport
from zip_archiver.reporter import JsonReporter


def test_generate_report(tmp_path) -> None:
    """Should generate JSON report."""

    output = tmp_path / "report.json"

    reporter = JsonReporter(output)

    report = ArchiveReport(
        archives_created=2,
        files_archived=10,
        total_original_size=10240,
        total_archive_size=4096,
    )

    reporter.generate(report)

    assert output.exists()

    data = json.loads(output.read_text())

    assert data["archives_created"] == 2
    assert data["files_archived"] == 10