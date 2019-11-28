import time
from concurrent.futures import ThreadPoolExecutor

#shared resource
num = 1


def run(workload):
    global num

    if num == 1:
        time.sleep(workload)
        num = num + 1
    return num


if __name__ == '__main__':
    workers = 5
    workload = 0  # change to 1

    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(run, [workload] * workers)

    print(list(res))
