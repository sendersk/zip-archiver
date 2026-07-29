from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field


class ArchiveConfig(BaseModel):
    """Archive configuration."""

    date_source: str = Field(
        default="modified",
        description="Source of the file date (modified, created, filename).",
    )

    remove_originals: bool = Field(
        default=False,
        description="Remove files after successful archiving.",
    )


class AppConfig(BaseModel):
    """Application configuration."""

    archive: ArchiveConfig


class ArchiveEntry(BaseModel):
    """Represents a single archive."""

    year: int
    archive_name: str
    files: list[Path]


class ArchiveDetails(BaseModel):
    """Detailed statistics for a single archive."""

    year: int
    archive_name: str

    files: int

    original_size: int
    archive_size: int

    saved_space: int
    compression_ratio: float


class ArchiveConfiguration(BaseModel):
    """Configuration snapshot used during execution."""

    recursive: bool
    date_source: str
    remove_originals: bool
    compression: str


class ArchiveReport(BaseModel):
    """Complete archive execution report."""

    timestamp: datetime | None = None

    duration_ms: int = 0

    directories_scanned: int = 0
    files_scanned: int = 0

    archives_created: int = 0

    files_archived: int = 0
    files_skipped: int = 0
    files_failed: int = 0

    total_original_size: int = 0
    total_archive_size: int = 0

    saved_space: int = 0
    compression_ratio: float = 0.0

    archives: list[ArchiveDetails] = []

    configuration: ArchiveConfiguration | None = None