import pytest

from ..find_if_index_and_element_are_equal import index_and_element_equal


@pytest.mark.parametrize('x, expected', [
    ([0, 2, 5, 6], 0),
    ([8, 2, 5, 6], None),
    ([10, 1, 2, 3, 4, 4], 4)

])
def test_index_and_element_equal(x, expected):
    actual = index_and_element_equal(x)
    assert actual == expected
