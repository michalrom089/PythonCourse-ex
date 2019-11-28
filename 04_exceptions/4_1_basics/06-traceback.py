import sys
import logging
import traceback


def divide(x, y):
    traceback.print_stack()
    return x/y


def get_speed(s, t):
    s = divide(s, t)
    return s


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    s = 10
    t = 2

    get_speed(s, t)
