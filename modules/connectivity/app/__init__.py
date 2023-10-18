import logging, sys

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(filename)s:%(asctime)s %(message)s', datefmt='%d/%m/%Y, %H:%M:%S,')

stderr_handler = logging.StreamHandler(sys.stderr)

stderr_handler.setFormatter(formatter)
logger.addHandler(stderr_handler)