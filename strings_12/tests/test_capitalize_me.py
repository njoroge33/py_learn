import pytest
from ..capitalize_me import cap


@pytest.mark.parametrize("x_str, expected", [
    ("john", "John"),
    ("peter", "Peter")
])
def test_capitalize_me(x_str, expected):
    actual = cap(x_str)
    assert actual == expected
