from contextlib import suppress
import os
import sys
import logging


def delete_file():
    os.remove('somefile.tmp')


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    try:
        with suppress(FileNotFoundError):
            delete_file()
        print('No exception raised')
    except Exception:
        logging.exception('Unknown exception has been raised.')