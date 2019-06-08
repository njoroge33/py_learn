import pytest
from ..sumnumberits_different import sum_digits


@pytest.mark.parametrize("x_str, expected", [
    ("john33", 6),
    ("peter", 0),
    ("2fry4", 6)
])
def test_sum_digits(x_str, expected):
    actual = sum_digits(x_str)
    assert actual == expected
