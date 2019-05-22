import pytest
from ..multiply import multiply


@pytest.mark.parametrize("num_1, num_2, expected", [
    (10, 2, 20),
    (11, 4, 44),
    (9, 3, 27)
])
def test_multiply(num_1, num_2, expected):
    actual = multiply(num_1, num_2)
    assert actual == expected
