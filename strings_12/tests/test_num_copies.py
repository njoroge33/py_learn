import pytest
from ..num_copies import num_copies


@pytest.mark.parametrize("x_str, num, expected", [
    ("hi", 2, "hihi"),
    ("cross", 1, "cross"),
    ("cross", 3, "crosscrosscross")
])
def test_num_copies(x_str, num, expected):
    actual = num_copies(x_str, num)
    assert actual == expected
