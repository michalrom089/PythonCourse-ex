import logging
import sys


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info(f"Setting {key} equals {value}")
        super().__setitem__(key, value)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    l_dict = LoggingDict()
    l_dict[3] = 'value3'
    l_dict[2] = 'value2'

    print(l_dict)
