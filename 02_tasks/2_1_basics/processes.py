import time
import multiprocessing
from timeit import default_timer as timer

process_information = ""


def run(n):
    global process_information
    process_information = 'process'

    for i in range(10):
        time.sleep(1)
        print(i)

    time.sleep(n)


if __name__ == '__main__':
    # multiprocess debugging requires spawn method
    # @ref: https://github.com/microsoft/ptvsd/blob/master/TROUBLESHOOTING.md#1-multiprocessing-on-linuxmac
    multiprocessing.set_start_method('spawn', True)

    start = timer()

    workload = 1
    p1 = multiprocessing.Process(target=run, args=(workload,))
    p2 = multiprocessing.Process(target=run, args=(workload,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = timer()

    print(
        {
            'info': process_information,
            'exec_time': end-start
        }
    )
