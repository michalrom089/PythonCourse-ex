from functools import wraps


def split_string(func):
    @wraps(func)
    def wrapped():
        result = func()
        return result.split(',')

    return wrapped


@split_string
def hello():
    return 'hello, steve'


@split_string
def greet():
    return 'greet, radek'


if __name__ == '__main__':
    print(hello())
    print(greet())
