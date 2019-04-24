import pytest

from ..reverse_list import reverse_list


@pytest.mark.parametrize('arr_x, expected', [
    ([5, 6, 6, 7, 3], [3, 7, 6, 6, 5]),
    ([23, 40, 10, 34], [34, 10, 40, 23]),
    ([2, 57, 23], [23, 57, 2])
])
def test_reverse_list(arr_x, expected):
    actual = reverse_list(arr_x)
    assert actual == expected
