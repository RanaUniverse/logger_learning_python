"""
This is for learning how the logger works
"""

from utils.custom_logger import logging


first_name = "Rana"
last_name = "Universe"

full_name = first_name + " " + last_name

logging.debug(f"The Logger is for: {full_name.upper()}")


donuts = int(input("Enter total donuts: "))
guests = int(input("Enter number of guests: "))


try:
    donuts_per_guest = donuts / guests
    logging.info(
        f"Calculation successful: Each guest gets {donuts_per_guest:.2f} donuts"
    )
except ZeroDivisionError:
    logging.error("Donut Calculation Error", exc_info=True)
    logging.error("Donut Calculation Error without full info")
