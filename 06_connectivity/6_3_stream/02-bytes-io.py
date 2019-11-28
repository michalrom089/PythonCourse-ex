
if __name__ == '__main__':

    f = open('./06-connectivity/6.3-stream/input.txt', 'r')

    print(f"\ncurrent_pos: {f.tell()}\n")
    print(f.read(1))
    print(f"\ncurrent_pos: {f.tell()}\n")

    f.close()
