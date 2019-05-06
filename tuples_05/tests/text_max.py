import pytest
from ..max import tup_max

@pytest.mark.parametrize('tuple_x, expected', [
    ((23, 13, 8, 6), 23),
    ((3, 8, 4, 6), 8),
    ((4, 14, 3, 8), 14)
])
def test_max(tuple_x, expected):
    actual = tup_max(tuple_x)
    assert actual == expected
