from functools import wraps


def logged(func):
    @wraps(func)
    def wrapped():
        print(f"Executed {func.__name__}")
        func()

    return wrapped


@logged
def hi(name='Steve'):
    print(f"Hi {name}")


if __name__ == '__main__':
    hi()

    print(hi.__name__)
