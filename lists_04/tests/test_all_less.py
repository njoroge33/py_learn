import pytest

from ..allless import all_less


@pytest.mark.parametrize('x, y, expected'
                         '', [
    ([1, 2, 3], [4, 5, 6, 7], False),
    ([4, 1, 7, 9], [5, 6, 8, 0], False),
    ([2, 3], [3, 4, 5], False)
])
def test_all_less(x, y, expected):
    actual = all_less(x, y)
    assert actual == expected
