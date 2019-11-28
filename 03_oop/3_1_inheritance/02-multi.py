import sys
from pprint import pprint
import collections
import logging


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info(f"Setting {key} equals {value}")
        super().__setitem__(key, value)


class OrderedLoggingDict(LoggingDict, collections.OrderedDict):
    pass


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    l_dict = OrderedLoggingDict()
    l_dict[3] = 'value3'
    l_dict[1] = 'value3'

    print(l_dict)

    # Method Resolution Order
    pprint(OrderedLoggingDict.__mro__)
