import pytest
from calculator import divide


# 正常系：通常の入力
def test_divide_normal():
    assert divide(10, 2) == 5.0


# 異常系：例外が起きる入力
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# 境界値：特殊な値
def test_divide_very_small():
    result = divide(1, 1_000_000)
    assert result == pytest.approx(0.000001)


def test_divide_negative():
    assert divide(-10, 2) == -5.0
