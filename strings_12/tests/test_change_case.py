import pytest
from ..change_case import change_case


@pytest.mark.parametrize("x_str, expected", [
    ("BLACKstar", "blackSTAR"),
    ("peTerSon", "PEtERson")
])
def test_change_case(x_str, expected):
    actual = change_case(x_str)
    assert actual == expected
