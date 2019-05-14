import pytest

from ..unique_sum import unique_sum


@pytest.mark.parametrize('a, b, c, expected', [
    (1, 2, 3, 6),
    (4, 1, 1, 5),
    (2, 2, 2, 2)
])
def test_unique_sum(a, b, c, expected):
    actual = unique_sum(a, b, c)
    assert actual == expected
