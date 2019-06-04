import pytest
from ..palindrome_string import palindrome


@pytest.mark.parametrize("x_str, expected", [
    ("aka", True),
    ("dad", True),
    ("cross", False)
])
def test_palindrome_string(x_str, expected):
    actual = palindrome(x_str)
    assert actual == expected
