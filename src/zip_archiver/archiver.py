from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from zip_archiver.models import ArchiveEntry


class ZipArchiver:
    """Create ZIP archives from archive plans."""

    def create_archive(
            self,
            directory: Path,
            plan: ArchiveEntry,
    ) -> Path:
        """
        Create a ZIP archive from the provided archive plan.

        Args:
             directory: Root directory where the archive will be created.
             plan: Archive definition.

        Returns:
             Path to the created archive.
        """

        archive_plan = directory / plan.archive_name

        with ZipFile(
            archive_plan,
            mode="w",
            compression=ZIP_DEFLATED,
        ) as archive:
            for file in plan.files:
                archive.write(file, arcname=file.name)

        return archive_plan

    def verify_archive(
            self,
            archive_path: Path,
    ) -> bool:
        """
        Verify that a ZIP archive is valid.

        Args:
            archive_path: Path to the archive

        Returns:
            True if the archive is valid.
        """

        try:
            with ZipFile(archive_path) as archive:
                return archive.testzip() is None
        except Exception:
            return False