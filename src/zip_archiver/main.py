from pathlib import Path

import typer

from zip_archiver.archiver import ZipArchiver
from zip_archiver.config import load_config
from zip_archiver.date_resolver import FileDateResolver
from zip_archiver.planner import ArchivePlanner
from zip_archiver.scanner import FileScanner

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
) -> None:
    """Archive old files."""

    config = load_config()

    scanner = FileScanner(directory)
    resolver = FileDateResolver()

    planner = ArchivePlanner(
        resolver,
        config.archive.date_source,
    )

    archiver = ZipArchiver()

    files = scanner.scan()

    plans = planner.create_plan(directory, files)

    for plan in plans:

        if dry_run:
            typer.echo(f"[DRY-RUN] {plan.archive_name}")

            for file in plan.files:
                typer.echo(f"   - {file.name}")

            continue

        archiver.archive(
            directory,
            plan,
            remove_originals=config.archive.remove_originals,
        )

        typer.echo(f"Created {plan.archive_name}")

        typer.echo()
        typer.echo("Archive process completed.")
        typer.echo(f"Archives created: {len(plans)}")



@app.command()
def version() -> None:
    """Show application version."""

    typer.echo("zip-archiver 0.1.0")


def main() -> None:
    """Application entry point."""

    app()


if __name__ == "__main__":
    main()