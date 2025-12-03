import inspect
import logging


logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.DEBUG)


def call(instance, *args):
    if len(args):
        logging.debug("{}.{}({})".format(type(instance).__name__, inspect.stack()[1][3], args))
    else:
        logging.debug("{}.{}()".format(type(instance).__name__, inspect.stack()[1][3]))
