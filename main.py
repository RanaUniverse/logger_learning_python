'''
This is for learning how the logger works
'''

first_name = "Rana"
last_name = "Universe"

full_name = first_name + " " + last_name

from utils.custom_logger import logging

logging.debug(f"The Logger is for: {full_name.upper()}")