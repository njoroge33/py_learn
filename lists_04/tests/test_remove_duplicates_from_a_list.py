import pytest

from ..remove_duplicates_from_a_list import remove_duplicates


@pytest.mark.parametrize('arr_x, expected', [
    ([2, 3, 3, 4, 5, 6, 6, 7, 3], [2, 3, 4, 5, 6, 7]),
    ([2, 3, 10, 23, 40, 10, 34], [2, 3, 10, 23, 40, 34]),
    ([2, 3, 11, 23, 40, 10, 34], [2, 3, 11, 23, 40, 10, 34])
])
def test_remove_duplicates(arr_x, expected):
    actual = remove_duplicates(arr_x)
    assert actual == expected
