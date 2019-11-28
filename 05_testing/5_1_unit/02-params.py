import pytest


def divide(a, b):
    return a/b


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 0.5),
        (4, 2, 2),
        (10, 2, 5)
    ],
)
def test_add(a, b, expected):
    # Act
    r = divide(a, b)

    # Assert
    assert r == expected
