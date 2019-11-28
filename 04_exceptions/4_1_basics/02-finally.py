import sys
import logging


if __name__ == "__main__":
    # setup logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    try:
        print(0/0)
    except Exception:
        logging.exception('Format failed')
    finally:
        logging.info('Program has returned 0')
