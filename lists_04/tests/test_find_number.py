import pytest

from ..find_number import find_number


@pytest.mark.parametrize('x, y, expected', [
    ([0, 2, 5, 6], 0, 0),
    ([8, 2, 5, 6], 9, None),
    ([10, 1, 2, 3, 4, 4], 4, 4)

])
def test_find_number(x, y, expected):
    actual = find_number(x, y)
    assert actual == expected
