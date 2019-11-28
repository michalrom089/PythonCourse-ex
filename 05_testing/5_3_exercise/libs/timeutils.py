from datetime import datetime, timedelta


def get_yesterday(fmt=None):
    t = (datetime.today() - timedelta(days=1))
    if fmt is not None:
        t = t.strftime(fmt)
    return t


def get_today(fmt=None):
    t = datetime.today()
    if fmt is not None:
        t = t.strftime(fmt)
    return t


def get_last_weekday(weekday_num=0, fmt=None):
    """ Get last weekday date:

        Args:
            weekday_num(int):  the day of the week as an integer, where Monday is 0 and Sunday is 6
            fmt(String): datetime strftime format
    """

    if(weekday_num > 6):
        raise Exception('Invalid weekday')

    today = get_today()
    weekdays = 7

    days_diff = today.weekday() - weekday_num
    if today.weekday() < weekday_num:
        days_diff = days_diff + weekdays

    t = today - timedelta(days=days_diff)

    if fmt is not None:
        t = t.strftime(fmt)
    return t
