import re

from datetime import datetime
from pathlib import Path


class FileDateResolver:
    """Resolve the year associated with a file."""

    YEAR_PATTERN = re.compile(r"(20\d{2})")

    def get_modified_year(self, file: Path) -> int:
        """Return the file modification year."""

        return datetime.fromtimestamp(file.stat().st_mtime).year

    def get_created_year(self, file: Path) -> int:
        """Return the file creation year."""

        return datetime.fromtimestamp(file.stat().st_ctime).year

    def get_filename_year(self, file: Path) -> int | None:
        """Extract year from filename."""

        match = self.YEAR_PATTERN.search(file.stem)

        if match:
            return int(match.group())

        return None

    def resolve_year(self, file: Path, source: str = "modified") -> int | None:
        """
        Resolve the year using the selected strategy.

        Args:
            file: File path.
            source: Year source (modified, created, filename).

        Returns:
             Resolved year or None.
        """

        match source:
            case "modified":
                return self.get_modified_year(file)
            case "created":
                return self.get_created_year(file)
            case "filename":
                return self.get_filename_year(file)
            case _:
                raise ValueError(f"Unknown date source: {source}")