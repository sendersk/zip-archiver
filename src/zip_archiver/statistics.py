from pathlib import Path

from zip_archiver.models import (
    ArchiveConfiguration,
    ArchiveDetails,
    ArchiveEntry,
    ArchiveReport,
)


class ArchiveStatistics:
    """Build archive execution reports."""

    def _calculate_sizes(
        self,
        archive_path: Path,
        plan: ArchiveEntry,
    ) -> tuple[int, int]:
        """
        Calculate original and archive sizes.

        Args:
            archive_path: Created archive.
            plan: Archive plan.

        Returns:
            Tuple containing original size and archive size.
        """

        original_size = sum(
            file.stat().st_size
            for file in plan.files
            if file.exists()
        )

        archive_size = (
            archive_path.stat().st_size
            if archive_path.exists()
            else 0
        )

        return original_size, archive_size

    def _build_archive_details(
        self,
        archive_path: Path,
        plan: ArchiveEntry,
    ) -> ArchiveDetails:
        """
        Build statistics for a single archive.

        Args:
            archive_path: Path to archive.
            plan: Archive definition.

        Returns:
            ArchiveDetails instance.
        """

        original_size, archive_size = self._calculate_sizes(
            archive_path,
            plan,
        )

        return ArchiveDetails(
            year=plan.year,
            archive_name=plan.archive_name,
            files=len(plan.files),
            original_size=original_size,
            archive_size=archive_size,
            saved_space=0,
            compression_ratio=0.0,
        )

    def _create_configuration(
        self,
        recursive: bool,
        date_source: str,
        remove_originals: bool,
    ) -> ArchiveConfiguration:
        """
        Create configuration snapshot.

        Args:
            recursive: Recursive scan enabled.
            date_source: Source of file date.
            remove_originals: Remove files after archiving.

        Returns:
            ArchiveConfiguration model.
        """

        return ArchiveConfiguration(
            recursive=recursive,
            date_source=date_source,
            remove_originals=remove_originals,
            compression="ZIP_DEFLATED",
        )

    def create_report(
        self,
        archives: list[Path],
        plans: list[ArchiveEntry],
        *,
        duration_ms: int,
        recursive: bool,
        date_source: str,
        remove_originals: bool,
        files_scanned: int,
        directories_scanned: int,
        files_skipped: int = 0,
        files_failed: int = 0,
    ) -> ArchiveReport:
        """
        Build complete archive execution report.

        Args:
            archives: Created archives.
            plans: Archive plans.
            duration_ms: Execution time.
            recursive: Recursive scan enabled.
            date_source: File date source.
            remove_originals: Remove archived files.
            files_scanned: Number of scanned files.
            directories_scanned: Number of scanned directories.
            files_skipped: Skipped files.
            files_failed: Failed files.

        Returns:
            ArchiveReport instance.
        """

        archive_details: list[ArchiveDetails] = []

        total_original_size = 0
        total_archive_size = 0

        for archive_path, plan in zip(archives, plans, strict=False):

            details = self._build_archive_details(
                archive_path,
                plan,
            )

            archive_details.append(details)

            total_original_size += details.original_size
            total_archive_size += details.archive_size

        configuration = self._create_configuration(
            recursive=recursive,
            date_source=date_source,
            remove_originals=remove_originals,
        )

        return ArchiveReport(
            timestamp=None,          # Added in commit #9.5
            duration_ms=duration_ms,
            directories_scanned=directories_scanned,
            files_scanned=files_scanned,
            archives_created=len(archives),
            files_archived=sum(
                len(plan.files)
                for plan in plans
            ),
            files_skipped=files_skipped,
            files_failed=files_failed,
            total_original_size=total_original_size,
            total_archive_size=total_archive_size,
            saved_space=0,
            compression_ratio=0.0,
            archives=archive_details,
            configuration=configuration,
        )