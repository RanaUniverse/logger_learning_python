"""
This is utils.new_logger.py file
I make this for checking how this will work
"""

import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(
    "app.log",
    mode="a",
    encoding="utf-8",
)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

formatter1 = logging.Formatter(
    "{levelname} - {message}",
    style="{",
)
formatter2 = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handler.setFormatter(formatter1)
file_handler.setFormatter(formatter2)


if __name__ == "__main__":
    logger.debug("Somethings Happens")
