import threading
from random import random


c = threading.Condition()
resources = []


def produce():
    r = random()
    c.acquire()
    resources.append(r)  # appends random number
    print(f"Releasing {r}")
    c.notify()
    c.release()  # increments internal counter


def consume():
    c.acquire()
    c.wait() # releasing lock until c.notify()
    r = resources.pop(0)
    print(f'Consuming {r}')
    c.release()


if __name__ == '__main__':
    tasks = [
        threading.Thread(target=consume),
        threading.Thread(target=consume),
        threading.Thread(target=produce),
        threading.Thread(target=produce),
        threading.Thread(target=consume),
        threading.Thread(target=produce)
    ]

    for t in tasks:
        t.start()

    for t in tasks:
        t.join()
