import typer

app = typer.Typer(
    help="Archive files from previous years into ZIP archives."
)


@app.command()
def version() -> None:
    """Show application version."""

    typer.echo("zip-archiver 0.1.0")


def main() -> None:
    """Application entry point."""

    app()


if __name__ == "__main__":
    main()