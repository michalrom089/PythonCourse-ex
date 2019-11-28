import sys
import logging
from functools import wraps


def requires_auth(f):
    @wraps(f)
    def wrapped(self, *args, **kwargs):
        if self.identity == 'Steve':
            logging.info("Authorization passed")
        else:
            raise SystemError('Unauthorized')
        return f(self, *args, **kwargs)
    return wrapped


class Computer:
    def login(self, identity):
        self.identity = identity

    @requires_auth
    def format(self):
        logging.warning('Computer has been formated')


if __name__ == "__main__":
    # setup logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    c = Computer()
    c.login('Steve')
    c.format()
