from pathlib import Path

import typer

from zip_archiver.archiver import ZipArchiver
from zip_archiver.config import load_config
from zip_archiver.date_resolver import FileDateResolver
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

    # Load application configuration
    config = load_config()

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

    # Create archive plan
    plans = planner.create_plan(directory, files)

    created_archives: list[Path] = []

    if not plans:
        typer.echo("No files eligible for archiving.")
        return

    # Execute archive plan
    for plan in plans:

        if dry_run:
            typer.echo(f"[DRY-RUN] {plan.archive_name}")

            if verbose:
                for file in plan.files:
                    typer.echo(f"   - {file.name}")

            continue

        archive_path = archiver.archive(
            directory,
            plan,
            remove_originals=config.archive.remove_originals,
        )

        created_archives.append(archive_path)

        typer.echo(f"Created {archive_path.name}")

        if verbose:
            for file in plan.files:
                typer.echo(f"   - {file.name}")

    # Skip report generation in dry-run mode
    if dry_run:
        typer.echo()
        typer.echo("Dry-run completed.")
        typer.echo(f"Archives planned: {len(plans)}")
        return

    # Generate archive statistics
    report = statistics.create_report(
        created_archives,
        plans,
    )

    # Save JSON report
    reporter = JsonReporter(
        directory / "reports" / "archive_report.json"
    )

    reporter.generate(report)

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