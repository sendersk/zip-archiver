import json
from pathlib import Path

from zip_archiver.models import ArchiveReport


class JsonReporter:
    """Generate archive reports in JSON format."""

    def __init__(self, output: Path) -> None:
        self.output = output

    def generate(self, report: ArchiveReport) -> None:
        """
        Save report to disk.

        Args:
            report: Archive execution summary.
        """

        self.output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.output.write_text(
            report.model_dump_json(indent=4),
            encoding="utf-8",
        )