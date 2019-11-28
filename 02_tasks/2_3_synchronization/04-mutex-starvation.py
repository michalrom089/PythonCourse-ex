import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock as Mutex


m = Mutex()
num = 0


def run(workload):
    global num, m

    with m:
        time.sleep(0.1)
        with open('04-mutex-starcation.txt') as f:
            f.write(workload)


if __name__ == '__main__':
    workers = 5
    workload = 1

    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(run, [workload] * 300)
