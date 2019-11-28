import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock as Mutex


m = Mutex()
num = 1


def run(inc):
    global num, m

    if num == 1:
        with m:
            if num == 1:
                time.sleep(1)
                num = num + inc

    return num


if __name__ == '__main__':
    workers = 5
    inc = 1

    with ProcessPoolExecutor(max_workers=workers) as executor:
        res = executor.map(run, [inc] * 5)

    print(list(res))
