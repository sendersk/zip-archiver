from datetime import UTC, datetime
from pathlib import Path

from zip_archiver.models import (
    ArchiveConfiguration,
    ArchiveDetails,
    ArchiveEntry,
    ArchiveReport,
)


DEFAULT_COMPRESSION = "ZIP_DEFLATED"


class ArchiveStatistics:
    """Build archive execution reports."""

    @staticmethod
    def _calculate_sizes(
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

    @staticmethod
    def _calculate_saved_space(
        original_size: int,
        archive_size: int,
    ) -> int:
        """
        Calculate saved disk space.

        Args:
            original_size: Total size of original files.
            archive_size: ZIP archive size.

        Returns:
            Saved space in bytes.
        """

        return max(original_size - archive_size, 0)

    @staticmethod
    def _calculate_compression_ratio(
        original_size: int,
        archive_size: int,
    ) -> float:
        """
        Calculate compression ratio.

        Args:
            original_size: Total size of original files.
            archive_size: ZIP archive size.

        Returns:
            Compression ratio as percentage.
        """

        if original_size == 0:
            return 0.0

        return round(
            (1 - archive_size / original_size) * 100,
            2,
        )

    def _build_archive_details(
        self,
        archive_path: Path,
        plan: ArchiveEntry,
    ) -> ArchiveDetails:
        """
        Build statistics for a single archive.
        """

        if not archive_path.exists():
            raise FileNotFoundError(f"Archive not found: {archive_path}")

        original_size, archive_size = self._calculate_sizes(
            archive_path,
            plan,
        )

        saved_space = self._calculate_saved_space(
            original_size,
            archive_size,
        )

        compression_ratio = self._calculate_compression_ratio(
            original_size,
            archive_size,
        )

        return ArchiveDetails(
            year=plan.year,
            archive_name=plan.archive_name,
            files=len(plan.files),
            original_size=original_size,
            archive_size=archive_size,
            saved_space=saved_space,
            compression_ratio=compression_ratio,
        )

    @staticmethod
    def _create_configuration(
        recursive: bool,
        date_source: str,
        remove_originals: bool,
    ) -> ArchiveConfiguration:
        """
        Create configuration snapshot.

        Args:
            recursive: Recursive scan enabled.
            date_source: Source of file date.
            remove_originals: Remove original files.

        Returns:
            ArchiveConfiguration instance.
        """

        return ArchiveConfiguration(
            recursive=recursive,
            date_source=date_source,
            remove_originals=remove_originals,
            compression=DEFAULT_COMPRESSION,
        )

    @staticmethod
    def _calculate_archive_count(
            archives: list[ArchiveDetails],
    ) -> int:
        """
        Calculate number of generated archives.

        Args:
            archives: Archive details list.

        Returns:
            Number of archives.
        """

        return len(archives)

    def create_report(
        self,
        archives: list[Path],
        plans: list[ArchiveEntry],
        *,
        duration_ms: int = 0,
        recursive: bool = False,
        date_source: str = "modified",
        remove_originals: bool = False,
        files_archived: int | None = None,
        files_scanned: int = 0,
        directories_scanned: int = 0,
        files_skipped: int = 0,
        files_failed: int = 0,
    ) -> ArchiveReport:
        """
        Build complete archive execution report.
        """

        archive_details: list[ArchiveDetails] = []

        total_original_size = 0
        total_archive_size = 0
        total_saved_space = 0

        for archive_path, plan in zip(
            archives,
            plans,
            strict=True,
        ):
            details = self._build_archive_details(
                archive_path,
                plan,
            )

            archive_details.append(details)

            archive_details.sort(key=lambda item: item.year)

            total_original_size += details.original_size
            total_archive_size += details.archive_size
            total_saved_space += details.saved_space

        overall_ratio = self._calculate_compression_ratio(
            total_original_size,
            total_archive_size,
        )

        configuration = self._create_configuration(
            recursive=recursive,
            date_source=date_source,
            remove_originals=remove_originals,
        )

        return ArchiveReport(
            timestamp=datetime.now(UTC),
            duration_ms=duration_ms,
            directories_scanned=directories_scanned,
            files_scanned=files_scanned,
            archives_created=self._calculate_archive_count(archive_details),
            files_archived=(
                files_archived
                if files_archived is not None
                else sum(
                    len(plan.files)
                    for plan in plans
                )
            ),
            files_skipped=files_skipped,
            files_failed=files_failed,
            total_original_size=total_original_size,
            total_archive_size=total_archive_size,
            saved_space=total_saved_space,
            compression_ratio=overall_ratio,
            archives=archive_details,
            configuration=configuration,
        )