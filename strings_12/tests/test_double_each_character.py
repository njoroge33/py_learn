import pytest
from ..double_each_character import double_char


@pytest.mark.parametrize("x_str, expected", [
    ("john", "jjoohhnn"),
    ("marcus", "mmaarrccuuss"),
    ("cross", "ccrroossss")
])
def test_double_each_character(x_str, expected):
    actual = double_char(x_str)
    assert actual == expected
