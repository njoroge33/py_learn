import pytest

from ..roots import get_root


@pytest.mark.parametrize('x, n, expected', [
    (2, 9, 3),
    (4, 10000, 10),
    (2, 100, 10)
])
def test_get_root(x, n, expected):
    actual = get_root(x, n)
    assert actual == expected
