import pytest
from ..first_two import first_two


@pytest.mark.parametrize("x_str, expected", [
    ("robbin", "ro"),
    ("b", "b"),
    ("", "")
])
def test_first_two(x_str, expected):
    actual = first_two(x_str)
    assert actual == expected
