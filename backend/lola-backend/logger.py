# encoding: utf-8
import logging
import sys


def init_logger(logfile: str, level: int = logging.DEBUG):
    """Initialize the root logger and standard log handlers."""
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    sys.excepthook = log_uncaught_exception


def log_uncaught_exception(type, value, traceback):
    root_logger = logging.getLogger()
    root_logger.exception(f"Uncaught exception: {value}")
