import sys
import logging

def try_except()
    try:
        print(0/0)
    except CriticalException:
        return 1
    except Exception: # on exceptions
        logging.exception('Format failed')
    else: # there were no exceptions
        print('Exception was not raised')
    finally: # call all the time
        logging.info('Program has returned 0')


    return 0
if __name__ == "__main__":
    # setup logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


    result = try
    return 0: