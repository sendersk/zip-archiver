from pathlib import Path

from zip_archiver.config import load_config


def test_load_config(tmp_path: Path) -> None:
    """Should load valid YAML configuration."""

    config_file = tmp_path / "settings.yaml"

    config_file.write_text(
        """
    archive:
        date_source: modified
        remove_originals: false        
""",
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert config.archive.date_source == "modified"
    assert config.archive.remove_originals is False