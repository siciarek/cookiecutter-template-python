import logging


class Logger(logging.Logger):
    def __init__(self, name: str, level: int, fmt: str, datefmt: str):
        super().__init__(name, level)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        handler.setFormatter(formatter)
        self.addHandler(handler)
