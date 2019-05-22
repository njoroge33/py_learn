import pytest
from ..greatest_common_divisor import greatest_divisor


@pytest.mark.parametrize("num_1, num_2, expected", [
    (9, 12, 3),
    (6, 18, 6),
    (24, 108, 12),
    (9, 12, 3)
])
def test_greatest_common_divisor(num_1, num_2, expected):
    actual = greatest_divisor(num_1, num_2)
    assert actual == expected
