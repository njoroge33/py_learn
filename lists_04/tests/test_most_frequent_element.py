import pytest

from ..most_frequent_element import find_popular_item


@pytest.mark.parametrize('arr_x, expected', [
    ([2, 3, 3, 4, 5, 6, 6, 7, 3], 3),
    ([2, 3, 10, 23, 40, 10, 34], 10),
    ([2, 3, 11, 23, 40, 10, 34], None),
    ([2], 2)
])
def test_find_popular_item(arr_x, expected):
    actual = find_popular_item(arr_x)
    assert actual == expected
