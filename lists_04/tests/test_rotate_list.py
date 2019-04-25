import pytest

from ..sum_of_even import sum_even


@pytest.mark.parametrize('x, expected', [
    ([1, 2, 3], 2),
    ([4, 1, 7, 9], 4),
    ([2, 3, 3, 4, 5], 6)
])
def test_sum_even(x, expected):
    actual = sum_even(x)
    assert actual == expected
