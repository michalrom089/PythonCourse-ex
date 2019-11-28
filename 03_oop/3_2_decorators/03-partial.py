from functools import partial


def hi(name, title):
    print(f"Hello {title} {name}")


if __name__ == '__main__':
    greet_mrs = partial(hi, title='Mrs')

    greet_mrs("Elizabeth")