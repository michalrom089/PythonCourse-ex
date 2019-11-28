# Task synchronization excercise

Using inheritance write 3 classes:

* LoggingDict - loggs getting and setting dictionary element
* SortedDict - sorts entries by value
* SortedLoggingDict - sorting entries + loggs getting and setting entries

Tips:
* both LoggingDict and SortedDict should inherit from dict class
* use [__getitem__](https://docs.python.org/3.8/library/csv.html) and [__setitem__](https://docs.python.org/3/reference/datamodel.html#object.__setitem__) methods
* SortedDict could have its own list (you can use sort and enumerate)
* SortedDict need to override [__str__](https://docs.python.org/3/reference/datamodel.html#object.__str__) method

```python
import logging
import sys


class LoggingDict():
    # TODO: complete implementation
    pass


class SortedDict():
    """ Sorted dictionary, every entry is sorted in a ascending manner.

        Sorted dict has its own storage implementation. Adding or getting entries operates on the self.list property.
    """ 
    # TODO: complete implementation
    def __init__(self):
        self.list = []

    


class LoggingSortedDict():
    # TODO: complete implementation
    pass


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    s = LoggingSortedDict()

    s['a'] = 2
    s['b'] = 1
    s['b'] = 5
    s['c'] = 1

    print(s)
    print(s['a'])

```

Expected result:
```bash
INFO:root:Setting a=2
INFO:root:Setting b=1
INFO:root:Setting b=5
INFO:root:Setting c=1
{ 'c': 1, 'a': 2, 'b': 5 }
INFO:root:Getting a
2
```