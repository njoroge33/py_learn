import pytest
from ..front_again import front_end


@pytest.mark.parametrize("x_str, expected", [
    ("edited", True),
    ("ed", True),
    ("modem", False)
])
def test_front_again(x_str, expected):
    actual = front_end(x_str)
    assert actual == expected
