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

    def count_directories(self) -> int:
        """
        Count scanned directories.

        Returns:
            Number of scanned directories.
        """

        if not self.recursive:
            return 1

        return sum(
            1
            for item in self.directory.rglob("*")
            if item.is_dir()
        ) + 1