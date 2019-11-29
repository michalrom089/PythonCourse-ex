import json
import csv
import logging
import sys
import mimetypes

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ParsingDataException(Exception):
    """Base class for exceptions raised by get_data_array()"""
    pass


class ParsingJsonError(ParsingDataException):
    pass


class ParsingCsvError(ParsingDataException):
    pass


class UnknownTypeError(ParsingDataException):
    pass


class DataUnavailableError(ParsingDataException):
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
    allowed_types = ['application/json', 'text/csv']
    data = []

    # guess type
    try:
        with open(filepath, 'r') as f:
            f_type = mimetypes.guess_type(filepath)[0]
            logger.info(f"Recognized {f_type} extension.")

            # json
            if f_type == allowed_types[0]:
                data = json.load(f)

            # csv
            elif f_type == allowed_types[1]:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(dict(row))  # casting OrderedDict to dict

            # not recognized
            else:
                raise UnknownTypeError(f'Unknwon file type: {f_type}')

            if len(data) == 0:
                raise DataUnavailableError()

    except csv.Error as e:
        raise ParsingCsvError(e.args[0])

    except json.decoder.JSONDecodeError as e:
        raise ParsingJsonError(e.args[0])

    return data


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    # limit csv field size to raise an exception on corrupted.csv file
    csv.field_size_limit(40)
    result_code = 0

    ok_csv = 'ok.csv'
    ok_json = 'ok.json'
    corrupted_csv = 'corrupted.csv'
    corrupted_json = 'corrupted.json'
    img = 'flower.jpg'
    empty = 'empty.csv'

    filename = img
    path = f'04_exceptions/4_2_exercise/seeds/{filename}'

    try:
        d = get_data_array(path)
    except FileNotFoundError:
        logging.exception('File was not found')
    except UnknownTypeError:
        logging.exception('Unknown file extension')
        result_code = 2
    except DataUnavailableError:
        logger.exception('Empty file')
        result_code = 3
    except ParsingCsvError:
        logger.exception('Parsing csv error')
        result_code = 4
    except ParsingJsonError:
        logger.exception('Parsing json error')
        result_code = 5
    except Exception:
        logger.exception('Unknown exception')
        result_code = 6

    exit(result_code)
