import json
import pytest
import requests
from requests import Response
from datetime import datetime


@pytest.fixture
def worldtimeapi_mock(mocker):
    seed = {
        'unixtime': 1574165137.0
    }

    resp = Response()
    resp.status_code = 200
    resp._content = bytes(json.dumps(seed), encoding="utf-8")

    mocker.patch.object(requests, 'get')
    requests.get.return_value = resp


def parse_time():
    url = 'http://worldtimeapi.org/api/timezone/America/Argentina/Salta'
    now = datetime.min
    try:
        json = requests.get(url).json()
        now = datetime.fromtimestamp(json['unixtime'])
    except Exception as e:
        print(str(e))

    return now

# -----------


def test_parse_time(worldtimeapi_mock):
    # Act
    now = parse_time()
    print(now)

    # Assert
    assert isinstance(now, datetime)
    assert now != datetime.min
    assert now.timestamp() == 1574165137.0
