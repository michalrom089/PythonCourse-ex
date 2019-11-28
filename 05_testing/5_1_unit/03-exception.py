import pytest


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError()

    if not isinstance(x, int) \
       or not isinstance(y, int):
        raise ValueError("Can't divide by non-integer")

    return x/y

# -----------


def test_divide_zero_division():
    # Assign
    a = 2
    b = 0

    # Assert
    with pytest.raises(ZeroDivisionError):
        divide(a, b)


def test_divide_value_error():
    # Assign
    a = 2
    b = '1'

    # Assert
    with pytest.raises(ValueError):
        divide(a, b)
