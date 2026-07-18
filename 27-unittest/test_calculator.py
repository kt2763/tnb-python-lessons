import pytest
from calculator import add, divide


def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_float():
    assert add(0.1, 0.2) == pytest.approx(0.3)  # 浮動小数点の比較


def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    import pytest

    with pytest.raises(ValueError, match="ゼロで割ることはできません"):
        divide(10, 0)
