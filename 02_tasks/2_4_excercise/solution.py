import sys
import random
import logging
import threading

c = threading.Condition()
s = threading.Semaphore(value=0)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
resources = []


def producer():
    """ Producer thread, append two item to the resources
    """

    logger = logging.getLogger(producer.__name__)

    r1 = random.random()
    r2 = random.random()

    with c:
        resources.append(r1)
        resources.append(r2)
        c.notify()

    logger.info(f'Added two items: {r1} and {r2}')


def big_consumer():
    """ Big Consumer thread, consumes three items from the resources
    """
    global resources

    logger = logging.getLogger(big_consumer.__name__)

    with c:
        while len(resources) < 3:
            c.wait()
        r = resources[0:3]
        resources = resources[3:]

    logger.info(f'Consumed 3 items: {r}')


def small_consumer():
    """ Small Consumer thread, consumes one items from the resources
    """
    logger = logging.getLogger(small_consumer.__name__)

    with c:
        logger.info('waiting for the item')
        while len(resources) < 1:
            c.wait()
        r = resources.pop(0)

    logger.info(f'Consumed 1 item: {r}')


if __name__ == '__main__':
    """ Run following threads (in random order):
            - 1 big_consumers
            - 3 small_consumers
            - 3 producers
    """
    tasks = [
        threading.Thread(target=producer),
        threading.Thread(target=producer),
        threading.Thread(target=big_consumer),
        threading.Thread(target=producer),
        threading.Thread(target=small_consumer),
        threading.Thread(target=small_consumer),
        threading.Thread(target=small_consumer),
    ]

    for t in tasks:
        t.start()

    for t in tasks:
        t.join()

    assert len(resources) == 0
