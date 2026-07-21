from collections import defaultdict
from pathlib import Path

from zip_archiver.date_resolver import FileDateResolver
from zip_archiver.models import ArchiveEntry


class ArchivePlanner:
    """Create an archive plan based on file years."""

    def __init__(self, resolver: FileDateResolver, date_source: str = "modified",) -> None:
        self.resolver = resolver
        self.date_source = date_source

    def create_plan(self, directory: Path, files: list[Path],) -> list[ArchiveEntry]:
        """
        Group files by year.

        Args:
            directory: Root directory.
            files: Files to process.

        Returns:
            Archive plan.
        """

        grouped: dict[int, list[Path]] = defaultdict(list)

        for file in files:
            year = self.resolver.resolve_year(file, self.date_source)

            if year is None:
                continue

            grouped[year].append(file)

        plans: list[ArchiveEntry] = []

        for year, items in sorted(grouped.items()):
            plans.append(
                ArchiveEntry(
                    year=year,
                    archive_name=f"{directory.name}_{year}.zip",
                    files=sorted(items),
                )
            )

        return plans