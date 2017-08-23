"""
https://docs.python.org/2/library/logging.html#logrecord-attributes
https://docs.python.org/2/library/time.html#time.strftime

"""
import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S %p', level=logging.DEBUG)

logging.warning("Warning Message")
logging.info("Info Message")
logging.error("Error Message")

