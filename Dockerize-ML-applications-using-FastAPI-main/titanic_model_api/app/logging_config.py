import logging
import sys
from typing import Any
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler

def setup_app_logging(config_path: Path) -> None:
    """Set up logging configuration for the application."""
    config = {
        "LOG_FORMAT": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "LOG_DIR": "logs",
        "LOG_LEVEL": "INFO",
    }

    # Create logs directory if it doesn't exist
    log_dir = Path(config.get("LOG_DIR", "logs"))
    log_dir.mkdir(exist_ok=True)

    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = TimedRotatingFileHandler(
        filename=log_dir / "titanic_api.log",
        when="midnight",
        interval=1,
        backupCount=7
    )

    # Create formatters and add it to handlers
    log_format = config.get("LOG_FORMAT")
    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the root logger
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Set log level
    root_logger.setLevel(config.get("LOG_LEVEL"))

def log_api_request(endpoint: str, request_data: Any = None) -> None:
    """Log API request details."""
    logger = logging.getLogger("api")
    logger.info(
        f"Request to {endpoint} - "
        f"Data: {request_data if request_data else 'No data'}"
    )

def log_api_response(endpoint: str, response_data: Any = None, error: bool = False) -> None:
    """Log API response details."""
    logger = logging.getLogger("api")
    level = logging.ERROR if error else logging.INFO
    logger.log(
        level,
        f"Response from {endpoint} - "
        f"{'Error' if error else 'Success'}: {response_data if response_data else 'No data'}"
    )