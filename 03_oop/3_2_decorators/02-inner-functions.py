def hi(name='Steve'):

    def hi_to_steve():
        print(f"Hi {name}")

    def welcome_anyone_else():
        print(f"Welcome {name}")

    if name == 'Steve':
        return hi_to_steve
    else:
        return welcome_anyone_else


if __name__ == '__main__':
    f1 = hi(name='Steve')
    f2 = hi(name='Jacob')

    f1()
    f2()