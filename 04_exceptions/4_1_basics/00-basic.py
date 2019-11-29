def div(a, b):
    if b == 0:
        raise Exception('dividing by 0')
    return a/b


if __name__ == '__main__':
    try:
        result = div(2, 0)
    except Exception as e:
        print(str(e))

    print('End of thre program')
