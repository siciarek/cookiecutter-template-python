import os
import logging
from pathlib import Path

APP_SHORT_NAME = "APP"

DEBUG = bool(int(os.getenv("DEBUG", "0")))
BASE_DIR = Path(__file__).parent.parent
BASE_MODULE_DIR = BASE_DIR / "section9tma"

CONFIG_DIR = BASE_DIR / "config"
TESTS_DIR = BASE_DIR / "tests"
TESTS_DATA_DIR = TESTS_DIR / "data"

CONFIG_BASE_DIR = TESTS_DATA_DIR if DEBUG else BASE_DIR

LOG_LEVELS = [
    logging.CRITICAL,
    logging.ERROR,
    logging.WARNING,
    logging.INFO,
    logging.DEBUG,
]

LOG_LEVEL = int(os.getenv("LOG_LEVEL", "4"))