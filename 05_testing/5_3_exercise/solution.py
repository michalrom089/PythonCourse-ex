import pytest
from datetime import datetime
from libs.timeutils import get_last_weekday


@pytest.fixture
def mock_get_today(mocker):
    today = datetime(2019, 11, 14)
    mocker.patch('libs.timeutils.get_today', return_value=today)


@pytest.mark.parametrize(
    "weekday_num, expected_datetime",
    [(0, datetime(2019, 11, 11)),
     (1, datetime(2019, 11, 12)),
     (2, datetime(2019, 11, 13)),
     (3, datetime(2019, 11, 14)),
     (4, datetime(2019, 11, 8)),
     (5, datetime(2019, 11, 9)),
     (6, datetime(2019, 11, 10)),
     pytest.param(7, datetime(2019, 11, 10), marks=pytest.mark.xfail)],
)
def test_get_last_weekday(weekday_num, expected_datetime, mock_get_today):
    # Act
    weekday = get_last_weekday(weekday_num)

    # Assert
    assert weekday.year == expected_datetime.year
    assert weekday.month == expected_datetime.month
    assert weekday.day == expected_datetime.day


def test_get_last_weekday_fmt(mock_get_today):
    # Arrange
    fmt = "%d-%b-%Y"
    weekday_num = 1

    weekday = get_last_weekday(weekday_num, fmt)

    assert weekday == '12-Nov-2019'
