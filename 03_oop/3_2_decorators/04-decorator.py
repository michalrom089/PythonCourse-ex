def logged(func):
    def wrapped():
        print(f"Executed {func.__name__}")
        func()

    return wrapped


@logged
def hi(name='Steve'):
    print(f"Hi {name}")

def wrapped():
    print(f"Executed {hi.__name__}")
    print(f"Hi Steve")


if __name__ == '__main__':
    hi()

    print(hi.__name__)

    # print(f"Function anem: {hi.__name__}")
