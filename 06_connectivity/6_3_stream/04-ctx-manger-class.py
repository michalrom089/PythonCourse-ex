from contextlib import contextmanager


class FileReader(object):
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        print('file opened')
        self.f = open(self.path, 'r')
        return self.f

    def __exit__(self, etype, value, traceback):
        print('file closed')
        print({
            'etype': etype,
            'value': value,
            'traceback': traceback
        })
        self.f.close()


if __name__ == '__main__':
    path = './06-connectivity/6.3-stream/input.txt'
    try:
        with FileReader(path) as f:
            # raise Exception('testexception')
            print(f.read())
    except Exception:
        pass
