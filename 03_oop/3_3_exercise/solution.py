import logging
import sys


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info(f"Setting {key}={value}")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        logging.info(f"Getting {key}")
        return super().__getitem__(key)


class SortedDict(dict):
    def __init__(self):
        self.list = []

    def __setitem__(self, key, value):
        i = None
        for idx, val in enumerate(self.list):
            if val[0] == key:
                i = idx

        # key not found -> append
        if i is None:
            self.list.append((key, value))
        # key found -> update
        else:
            self.list[i] = (key, value)

        self.list.sort(key=lambda val: val[1])

    def __getitem__(self, key):
        for t in self.list:
            if t[0] == key:
                return t[1]

        return None

    def __str__(self):
        s = "{"
        for t in self.list:
            s = s + f" '{t[0]}': {t[1]},"
        s = s[:-1] + ' }'

        return s


class LoggingSortedDict(LoggingDict, SortedDict):
    pass


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    s = LoggingSortedDict()

    s['a'] = 2
    s['b'] = 1
    s['b'] = 5
    s['c'] = 1

    print(s)
    print(s['a'])
