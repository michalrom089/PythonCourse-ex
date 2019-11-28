import sys
import logging


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError()

    if not isinstance(x, int) \
       or not isinstance(y, int):
        raise ValueError("Can't divide by non-integer")

    return x/y


if __name__ == "__main__":
    # setup logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    try:
        divide(1, '0')
    except ZeroDivisionError:
        logging.error("Can't divide by 0")
    except Exception:
        logging.exception('Unknown exception has been raised.')
