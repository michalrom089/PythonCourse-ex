from contextlib import contextmanager


@contextmanager
def read(file_path):
    try:
        print('file opened')
        f = open(file_path, 'r')
        yield f
    finally:
        print('file closed')
        f.close()


if __name__ == '__main__':
    path = './06-connectivity/6.3-stream/input.txt'
    with read(path) as f:
        print(f.read())
