import logging
from logging.config import dictConfig

class LogConfig:
    """Logging configuration to be set for the server"""

    LOG_FORMAT = "%(levelprefix)s | %(asctime)s | %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "fmt": LOG_FORMAT,
                "datefmt": DATE_FORMAT,
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "app": {"handlers": ["default"], "level": "INFO"},
        },
    }

def setup_logging():
    dictConfig(LogConfig.config)
