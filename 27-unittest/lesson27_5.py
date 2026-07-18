import pytest
from calculator import add, divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, -2, -3),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (7, 2, 3.5),
        (0, 5, 0.0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)
