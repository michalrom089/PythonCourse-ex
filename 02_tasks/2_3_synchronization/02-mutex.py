import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock as Mutex


m = Mutex()
num = 1


def run(workload):
    global num, m

    # critical section`
    m.acquire()
    if num == 1:
        time.sleep(workload)
        num = num + 1
    m.release()
  
    return num


if __name__ == '__main__':
    workers = 5`
    workload = 0

    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(run, [workload] * 5)

    print(list(res))
