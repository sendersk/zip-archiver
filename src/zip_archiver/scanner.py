from pathlib import Path


class FileScanner:
    """Scan directories and return files."""

    def __init__(
        self,
        directory: Path,
        recursive: bool = False,
    ) -> None:
        self.directory = directory
        self.recursive = recursive

    def scan(self) -> list[Path]:
        """
        Scan a directory for files.

        Returns:
            List of discovered files.
        """

        if self.recursive:
            files = [
                path
                for path in self.directory.rglob("*")
                if path.is_file()
            ]
        else:
            files = [
                path
                for path in self.directory.iterdir()
                if path.is_file()
            ]

        return sorted(files)