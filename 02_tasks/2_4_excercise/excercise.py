import sys
import random
import logging
import threading
from threading import Semaphore
 
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
 
logger=logging.getLogger(__name__)
resources = []
s = Semaphore(value=0)
 
def producer():
    """ Producer thread, append two item to the resources
    """
  
    for i in range(2):
        r = random.random()
        resources.append(r)
        logger.info(f"Produced an item: {r}")
        s.release()      
    pass
 
def big_consumer():
    """ Big Consumer thread, consumes three items from the resources
    """
    global resources
  
    consumed_items = []
 
    for i in range(3):
        s.acquire()
        item = resources.pop(0)
        consumed_items.append(item)
        
 
    logger.info(f"Consumed 3 items: {consumed_items} ")
    pass
 
def small_consumer():
    """ Small Consumer thread, consumes one items from the resources
    """
    s.acquire()
    product = resources.pop(0)
    logger.info(f"Consumed {product} item")
    
    pass
 
if __name__ == '__main__':
    """ Run following threads (in random order):
            - 1 big_consumers
            - 3 small_consumers
            - 3 producers
    """
    # TODO: run tasks in random order
 
    tasks = [
    threading.Thread(target=producer),
    threading.Thread(target=big_consumer),
    threading.Thread(target=small_consumer),
    threading.Thread(target=producer),
    ]
 
    for t in tasks:
        t.start()
 
    for t in tasks:
        t.join()
 
    assert len(resources) == 0