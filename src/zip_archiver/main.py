from pathlib import Path
from time import perf_counter

import typer

from zip_archiver.archiver import ZipArchiver
from zip_archiver.config import load_config
from zip_archiver.date_resolver import FileDateResolver
from zip_archiver.logging_config import setup_logging
from zip_archiver.planner import ArchivePlanner
from zip_archiver.reporter import JsonReporter
from zip_archiver.scanner import FileScanner
from zip_archiver.statistics import ArchiveStatistics


app = typer.Typer(
    help="Archive files from previous years into ZIP archives."
)


@app.command()
def archive(
        directory: Path = typer.Argument(
            ...,
            exists=True,
            file_okay=False,
            dir_okay=True,
            resolve_path=True,
            help="Directory to archive."
        ),
        dry_run: bool = typer.Option(
            False,
            "--dry-run",
            help="Preview archives without creating them."
        ),
        verbose: bool = typer.Option(
            False,
            "--verbose",
            help="Display processed files."
        ),
) -> None:
    """
    Archive files from previous years.
    """

    logger = setup_logging(Path("logs/app.log"))

    # Start execution timer
    start_time = perf_counter()

    # Load application configuration
    config = load_config()

    logger.info("Archive process started")

    # Initialize services
    scanner = FileScanner(directory)
    resolver = FileDateResolver()

    planner = ArchivePlanner(
        resolver,
        config.archive.date_source,
    )

    archiver = ZipArchiver()

    statistics = ArchiveStatistics()

    # Scan directory
    files = scanner.scan()

    logger.info(
        "Files scanned",
        extra={
            "files_count": len(files),
        },
    )

    files_scanned = len(files)

    directories_scanned = scanner.count_directories()

    files_archived = 0
    files_skipped = 0
    files_failed = 0

    # Create archive plan
    plans = planner.create_plan(directory, files)

    created_archives: list[Path] = []

    if not plans:
        typer.echo("No files eligible for archiving.")
        return

    # Execute archive plan
    for plan in plans:

        files_archived += len(plan.files)

        if dry_run:
            typer.echo(f"[DRY-RUN] {plan.archive_name}")

            if verbose:
                for file in plan.files:
                    typer.echo(f"   - {file.name}")

            continue
        try:
            archive_path = archiver.archive(
                directory,
                plan,
                remove_originals=config.archive.remove_originals,
            )

            created_archives.append(archive_path)

        except Exception as exc:
            logger.exception(
                "Archive creation failed",
                extra={
                    "error": str(exc),
                },
            )

            files_failed += 1
            continue

        typer.echo(f"Created {archive_path.name}")

        if verbose:
            for file in plan.files:
                typer.echo(f"   - {file.name}")

    files_skipped = files_scanned - files_archived

    # Skip report generation in dry-run mode
    if dry_run:
        typer.echo()
        typer.echo("Dry-run completed.")
        typer.echo(f"Archives planned: {len(plans)}")
        return

    duration_ms = int((perf_counter() - start_time) * 1000)

    # Generate archive statistics
    report = statistics.create_report(
        created_archives,
        plans,
        duration_ms=duration_ms,
        recursive=config.scan.recursive,
        date_source=config.archive.date_source,
        remove_originals=config.archive.remove_originals,
        files_scanned=len(files),
        directories_scanned=directories_scanned,
        files_skipped=files_skipped,
        files_failed=files_failed,
    )

    logger.info(
        "Archive created",
        extra={
            "archive": str(archive_path),
            "year": plan.year,
            "files": len(plan.files)
        },
    )

    # Save JSON report
    reporter = JsonReporter(
        directory / "reports" / "archive_report.json"
    )

    reporter.generate(report)

    logger.info(
        "Archive process completed",
        extra={
            "archives": len(created_archives),
            "duration_ms": duration_ms,
        },
    )

    typer.echo()
    typer.echo("Archive process completed.")
    typer.echo(f"Archives created: {len(created_archives)}")
    typer.echo(f"Report saved to: {directory / 'reports' / 'archive_report.json'}")


@app.command()
def version() -> None:
    """Show application version."""

    typer.echo("zip-archiver 0.1.0")


def main() -> None:
    """Application entry point."""

    app()


if __name__ == "__main__":
    main()