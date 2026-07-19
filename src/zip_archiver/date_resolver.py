import re

from datetime import datetime
from pathlib import Path


class FileDateResolver:
    """Resolve the year associated with a file."""

    YEAR_PATTERN = re.compile(r"(20\d{2})")

    def get_modified_year(self, file: Path) -> int:
        """
        Return the file modification year.

        Args:
            file: File path.

        Returns:
            Modification year.
        """

        timestamp = file.stat().st_mtime
        return datetime.fromtimestamp(timestamp).year

    def get_filename_year(self, file: Path) -> int | None:
        """
        Extract year from filename.

        Args:
            file: File path.

        Returns:
            Detected year or None.
        """

        match = self.YEAR_PATTERN.search(file.stem)

        if match:
            return int(match.group())

        return None