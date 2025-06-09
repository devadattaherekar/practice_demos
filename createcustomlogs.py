import logging
import createlogs as clogs


print(clogs.add(100,200))


# step 1 create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create stream handler and set level to debug
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# create file handler and set level to debug
fh = logging.FileHandler("custom_logs.txt")
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s %(message)s","Date is %d/%m/%Y and Time is %H:%M:%S")

# add formatter to stream handler
sh.setFormatter(formatter)
# add formatter to file handler
fh.setFormatter(formatter)

# add stream handler to logger
logger.addHandler(sh)
# add file handler to logger
logger.addHandler(fh)

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")


