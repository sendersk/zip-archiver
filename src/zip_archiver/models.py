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

    timestamp: datetime

    duration_ms: int

    directories_scanned: int
    files_scanned: int

    archives_created: int

    files_archived: int
    files_skipped: int
    files_failed: int

    total_original_size: int
    total_archive_size: int

    saved_space: int
    compression_ratio: float

    archives: list[ArchiveDetails]

    configuration: ArchiveConfiguration