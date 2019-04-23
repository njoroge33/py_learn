import pytest

from ..count_clumps import count_clumps


@pytest.mark.parametrize('x, expected', [
    ([1, 2, 2, 3, 4, 5], 1),
    ([1, 2, 2, 2, 4, 5], 1),
    ([1, 2, 4, 2, 4, 5], 0),
    ([1, 1, 1, 1, 1, 1], 1),
    ([1, 1, 2, 2, 3, 3], 3)
])
def test_count_clumps(x, expected):
    actual = count_clumps(x)
    assert actual == expected
