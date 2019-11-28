import requests
from datetime import datetime


def parse_time():
    url = 'http://worldtimeapi.org/api/timezone/America/Argentina/Salta'
    now = datetime.min

    try:
        json = requests.get(url).json()
        now = datetime.utcfromtimestamp(json['unixtime'])
    except Exception as e:
        print(str(e))

    return now

# -----------


def test_parse_time():
    # Act
    now = parse_time()

    # Assert
    assert isinstance(now, datetime)
    assert now != datetime.min
