from functools import partial


def hi(name, title):
    print(f"Hello {title} {name}")


if __name__ == '__main__':
    greet_mrs = partial(hi, title='Mrs')
    greet_mr = partial(hi, title='Mr')

    greet_mrs("Elizabeth")
    greet_mr('Radek')