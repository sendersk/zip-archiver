from pathlib import Path


class FileScanner:
    """Scan directories and return files."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def scan(self) -> list[Path]:
        """
        Scan a directory and return all files.

        Returns:
            List of discovered files.
        """

        return [path for path in self.directory.iterdir() if path.is_file()]