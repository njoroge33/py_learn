import pytest

from ..swap_ends import swap_ends


@pytest.mark.parametrize('x, expected', [
    ([1, 2, 3], [3, 2, 1]),
    ([4, 1, 7, 9], [9, 1, 7, 4]),
    ([2, 3, 3, 4, 5], [5, 3, 3, 4, 2])
])
def test_swap_ends(x, expected):
    actual = swap_ends(x)
    assert actual == expected
