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