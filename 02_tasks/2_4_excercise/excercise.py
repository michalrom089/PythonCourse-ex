import sys
import random
import logging
import threading


logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

resources = []


def producer():
    """ Producer thread, append two item to the resources
    """
  
    for i in range(2):
        r = random.random()
        resources.append(r)
        logger.info(f'Produced an item {r}')

    pass


def big_consumer():
    """ Big Consumer thread, consumes three items from the resources
    """
    global resources

    # consumed_items=[]
    # for i in range(3):
    #     item = resources.pop(0)
    #     consumed_items.append(item)

    consumed_items = resources[0:3] #slice notation works as a loop
    resources = resources[3:]
    
    logger.info(f'Consumed 3 items: {consumed_items}')

    pass


def small_consumer():
    """ Small Consumer thread, consumes one items from the resources
    """
    product = resources.pop(0)
    logger.info(f'Consumed {product} item')
    pass


if __name__ == '__main__':
    """ Run following threads (in random order):
            - 1 big_consumers
            - 3 small_consumers
            - 3 producers
    """

    # TODO: run tasks in random order

    producer()
    producer()
    big_consumer()
    small_consumer()

    assert len(resources) == 0

