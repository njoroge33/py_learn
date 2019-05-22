import pytest
from ..recursion_basics import fibo


@pytest.mark.parametrize("int_x, expected", [
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
])
def test_recursion_basics(int_x, expected):
    actual = fibo(int_x)
    assert actual == expected
