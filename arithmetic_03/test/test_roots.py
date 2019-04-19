import pytest

from ..roots import get_root


@pytest.mark.parametrize('x, n, expected', [
    (9, 2, 3.0),
    (10000, 4, 10),
    (32, 2, 5)
])
def test_get_root(x, n, expected):
    actual = get_root(x, n)
    assert actual == expected
