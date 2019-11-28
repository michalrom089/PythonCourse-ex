import sys
import logging


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError()

    if not isinstance(x, int) \
       or not isinstance(y, int):
        raise ValueError("Can't divide by non-integer")

    return x/y


def get_speed(s, t):
    """ Calc velocity V=S/t, uniform motion."""
    try:
        v = divide(s, t)
    except ZeroDivisionError:
        v = 0
    except Exception:
        raise

    return v


if __name__ == "__main__":
    # setup logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    s = 10
    t = 0

    print({'velocity': get_speed(s, t)})
