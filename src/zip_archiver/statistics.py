from pathlib import Path

from zip_archiver.models import ArchiveEntry, ArchiveReport


class ArchiveStatistics:
    """Calculate archive statistics."""

    def create_report(
            self,
            archives: list[Path],
            plans: list[ArchiveEntry],
    ) -> ArchiveReport:
        """
        Build archive summary.

        Args:
            archives: Created archive paths.
            plans: Archive plans.

        Returns:
            Archive report.
        """

        original_size = sum(
            file.stat().st_size
            for plan in plans
            for file in plan.files
            if file.exists()
        )

        archive_size = sum(
            archive.stat().st_size
            for archive in archives
            if archive.exists()
        )

        files_archived = sum(
            len(plan.files)
            for plan in plans
        )

        return ArchiveReport(
            archives_created=len(archives),
            files_archived=files_archived,
            total_original_size=original_size,
            total_archive_size=archive_size,
        )