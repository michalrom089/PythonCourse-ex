import sys
import logging
from functools import wraps


def logged(level):
    def decorator(func):
        @wraps(func)
        def wrapped():
            logging.log(level, f"Executed {func.__name__}")
            func()

        return wrapped
    return decorator


@logged(logging.DEBUG)
def hi(name='Steve'):
    print(f"Hi {name}")


if __name__ == '__main__':
    # setup logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    hi()
