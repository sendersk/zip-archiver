from pathlib import Path

import yaml

from zip_archiver.models import AppConfig


CONFIG_PATH = Path("config/settings.yaml")


def load_config(config_path: Path = CONFIG_PATH) -> AppConfig:
    """
    Load and validate application configuration.

    Args:
        config_path: Path to the YAML configuration file.

    Returns:
        Validated application configuration.
    """

    with config_path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return AppConfig.model_validate(data)