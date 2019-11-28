import pytest


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError()

    if not isinstance(x, int) \
       or not isinstance(y, int):
        raise ValueError("Can't divide by non-integer")

    return x/y

# -----------


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 0.5),
        (4, 2, 2),
        (10, 2, 5),
        pytest.param(1, 0, None, marks=pytest.mark.xfail(raises=ZeroDivisionError)),
        pytest.param(1, '0', None, marks=pytest.mark.xfail(raises=ValueError))
    ],
)
def test_add(a, b, expected):
    # Act
    r = divide(a, b)

    # Assert
    assert r == expected
