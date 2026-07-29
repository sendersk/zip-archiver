import json
import logging
import sys
from datetime import UTC, datetime
from pathlib import Path


class JsonFormatter(logging.Formatter):
    """Format logs as JSON."""

    def format(
            self,
            record: logging.LogRecord,
    ) -> str:
        """
        Convert log record into JSON format.

        Args:
            record: Logging record.

        Returns:
            JSON formatted log message.
        """

        log_data = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        return json.dumps(log_data)

def setup_logging(
        log_file: Path,
) -> logging.Logger:
    """
    Configure application logging.

    Args:
        log_file: Path to log file.

    Returns:
        Configured logger.
    """

    log_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger = logging.getLogger("zip_archiver")

    logger.setLevel(logging.INFO)

    logger.handlers.clear()

    formatter = JsonFormatter()

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)

    return logger