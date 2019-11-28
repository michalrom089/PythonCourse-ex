import sys
import logging


def divide(x, y):
    # TODO: replace AssertionError with ZeroDivisionError
    assert y != 0
    return x/y


if __name__ == "__main__":
    # setup logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    try:
        divide(0, 0)
    except Exception:
        logging.exception('Format failed')
    finally:
        logging.info('Program has returned 0')
