import pytest
from ..first_half_with_second_half import swap_char


@pytest.mark.parametrize("x_str, expected", [
    ("robbin", "binrob"),
    ("bob", "obb"),
    ("baba", "baba")
])
def test_first_half_with_second_half(x_str, expected):
    actual = swap_char(x_str)
    assert actual == expected
