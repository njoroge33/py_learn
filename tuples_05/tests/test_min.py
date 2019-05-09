import pytest
from ..min import tup_min


@pytest.mark.parametrize('tuple_x, expected', [
    ((23, 13, 8, 6), 6),
    ((3, 8, 4, 6), 3),
    ((4, 14, 3, 8, 2), 2)
])
def test_min(tuple_x, expected):
    actual = tup_min(tuple_x)
    assert actual == expected
