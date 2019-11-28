import dis


def hello():
    print('Hello World')


if __name__ == '__main__':
    dis.dis(hello)
