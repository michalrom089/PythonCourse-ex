# Unit-Testing exercise

Implement all possible test cases for [***get_last_weekday()***](./libs/timeutils.py) function. 

The functions accepts weekday_num (where 0=Monday, 1=Tuesday etc.) and fmt ([readme](https://docs.python.org/3/library/datetime.html#datetime.date.strftime), [readme1](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)). 

Test cases should cover:
* All weekday_num's (0-6)
* Raising an Exception (Invalid weekday)
* Usage of fmt (e.g. "%d-%b-%Y")

Regarding continuous nature of the time, you should mock ***get_today()*** (using [mocker.patch](https://docs.python.org/3/library/unittest.mock.html#patch)) to get predictable results.