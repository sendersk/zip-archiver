from datetime import datetime
from pathlib import Path


class FileDateResolver:
    """Resolve the year associated with a file."""

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