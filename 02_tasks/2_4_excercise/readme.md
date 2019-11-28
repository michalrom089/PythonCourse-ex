# Task synchronization excercise

Using Conditions objects ([readme](https://docs.python.org/3/library/threading.html#condition-objects)) write simple script that implements:

* Three types of threads (small_consumer, big_consumer and producer):
    * Producer produces 2 items per run
    * Small consumer consumes 1 item per run
    * Big consumer consumes 2 items per run
* Use logger

The goal is to synchronize access to shared resources (in that case the **resources** list, that producers append items to (e.g. random numbers) and consumers pops the resources and prints them).

```python
import sys
import random
import logging
import threading

resources = []


def producer():
    """ Producer thread, append two item to the resources
    """
    # TODO: complete implementation
    pass


def big_consumer():
    """ Big Consumer thread, consumes three items from the resources
    """
    # TODO: complete implementation
    pass


def small_consumer():
    """ Small Consumer thread, consumes one items from the resources
    """
    # TODO: complete implementation
    pass


if __name__ == '__main__':
    """ Run following threads (in random order):
            - 1 big_consumers
            - 3 small_consumers
            - 3 producers
    """

    # TODO: run tasks in random order

    assert len(resources) == 0

```