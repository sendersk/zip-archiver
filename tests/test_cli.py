from pathlib import Path

from typer.testing import CliRunner

from zip_archiver.main import app

runner = CliRunner()


def test_version() -> None:
    """Should display application version."""

    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert "zip-archiver" in result.output


def test_archive_dry_run(tmp_path: Path) -> None:
    """Should execute dry-run successfully."""

    (tmp_path / "invoice_2025.pdf").touch()

    result = runner.invoke(
        app,
        [
            "archive",
            str(tmp_path),
            "--dry-run",
        ],
    )

    assert result.exit_code == 0