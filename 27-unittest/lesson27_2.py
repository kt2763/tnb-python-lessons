import pytest
from calculator import divide


def test_list_equality():
    result = [1, 2, 3]
    expected = [1, 2, 4]
    assert result == expected
    # AssertionError:
    # assert [1, 2, 3] == [1, 2, 4]
    #   At index 2 diff: 3 != 4


def test_string_in():
    message = "Hello, World!"
    assert "World" in message


def test_approximately_equal():
    assert 0.1 + 0.2 == pytest.approx(0.3)  # 浮動小数点に必須


def test_exception_raised():
    with pytest.raises(ValueError):
        int("not a number")


def test_exception_message():
    with pytest.raises(ValueError, match="ゼロで割ること"):
        divide(10, 0)
