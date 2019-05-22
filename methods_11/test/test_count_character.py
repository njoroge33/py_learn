import pytest
from ..count_a_character import count_char


@pytest.mark.parametrize("x_str, char, expected", [
    ("gichuhi", "i", 2),
    ("attention", "t", 3),
    ("john", "g", 0)
])
def test_count_character(x_str, char, expected):
    actual = count_char(x_str, char)
    assert actual == expected
