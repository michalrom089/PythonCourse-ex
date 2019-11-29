import time
import threading
from timeit import default_timer as timer

thread_information = ""


def run(n):
    global thread_information
    thread_information = "thread"
    
    for i in range(10):
        time.sleep(n)
        print(i)



if __name__ == '__main__':
    start = timer()

    workload = 1
    t1 = threading.Thread(target=run, args=(workload,))
    t2 = threading.Thread(target=run, args=(workload,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = timer()

    print(
        {
            'info': thread_information,
            'exec_time': end-start
        }
    )
