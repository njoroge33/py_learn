import pytest
from ..recursion_basics import gen_series


@pytest.mark.parametrize("int_x, expected", [
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
])
def test_recursion_basics(int_x, expected):
    actual = gen_series(int_x)
    assert actual == expected
