import threading
from random import random

s = threading.Semaphore(value=0)
resources = []


def produce():
    r = random()
    resources.append(r)  # appends random number
    print(f"Releasing {r}")
    s.release()  # increments internal counter


def consume():
    s.acquire()
    r = resources.pop(0)
    print(f'Consuming {r}')


if __name__ == '__main__':
    tasks = [
        threading.Thread(target=consume),
        threading.Thread(target=consume),
        threading.Thread(target=consume),
        threading.Thread(target=produce),
        threading.Thread(target=produce),
        threading.Thread(target=produce),
        threading.Thread(target=consume)
    ]

    for t in tasks:
        t.start()

    for t in tasks:
        t.join()
