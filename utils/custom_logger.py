import logging

import time

logging.Formatter.converter = time.gmtime

# abc = logging.warning("Remain Calm!")
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(levelname)s:%(name)s:%(message)s",
# )

logging.basicConfig(
    level=logging.DEBUG,
    # format="{levelname}:{name}:{message}", style="{",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug("This is a debug msg")
logging.info("Info of the system is here")

logging.warning("This is for warning")
logging.error("Somethigns error happesn in my system")
logging.critical("This is the critical msg")
