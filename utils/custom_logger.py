import logging

import time

logging.Formatter.converter = time.gmtime

logging.basicConfig(
    level=logging.DEBUG,
    filename="rana.log",
    encoding="utf-8",
    filemode="a",
    # format="{levelname}:{name}:{message}", style="{",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)


if __name__ == "__main__":

    logging.debug("This is a debug msg")
    logging.info("Info of the system is here")

    logging.warning("This is for warning")
    logging.error("Somethigns error happesn in my system")
    logging.critical("This is the critical msg")
