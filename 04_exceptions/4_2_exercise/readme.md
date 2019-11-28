# Exceptions exercise


Implement get_data_array() function, that gets path to a file, reads the file and returns array of dict objects (see: docstring of the function). Function needs to recognize type of the file (use [mimetypes](https://docs.python.org/3.8/library/mimetypes.html) module). Allowed data types are json and csv (use [json.load](https://docs.python.org/3.8/library/json.html#json.load) and [csv.DictReader](https://docs.python.org/3.8/library/csv.html#csv.DictReader) modules to read the file). Moreover, create custom Exceptions hierarchy (create the base exception, e.g. 'ParsingDataException', all custom exceptions listed below should inherit from the base exception).


get_data_array() should raise following exceptions:
* **FileNotFound**(system built-in): filepath points to nothing
* **UnknownTypeError**(custom): file is not json or csv
* **DataUnavailableError**(custom): file contains no data
* **ParsingCsvError**(custom): parsing CSV file failed
* **ParsingJsonError**(custom): parsing JSON file failed

```python
import json
import csv
import logging
import sys
import mimetypes


class ParsingDataException(Exception):
    """Base class for exceptions raised by get_data_array()"""
    pass


def get_data_array(filepath):
    """ Read file as a list of dictionaries. Reads data saved as json or csv, other formats are not supported.

        Args:
            filepath(String): path to the file

        Returns:
            (list): list of dict object, e.g.
                [
                    {'id': 1, 'value': 10},
                    {'id': 2, 'value': 32},
                    {'id': 3, 'value': 132},
                    {'id': 4, 'value': 42}
                ]

        Exceptions:
            FileNotFound: filepath points to nothing
            UnknownTypeError: file is not json or csv
            DataUnavailableError: file contains no data
            ParsingCsvError: parsing CSV file failed
            ParsingJsonError: parsing JSON file failed
            Others: exits with code 1
    """

    # TODO: complete implementation
    pass

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    # limit csv field size to raise an exception on corrupted.csv file
    csv.field_size_limit(40)

    # TODO: determine path to every file
    d = get_data_array(path)

```