import pytest

from ..reverse_lists import reverse_lists


@pytest.mark.parametrize('arr_x, expected', [
    ([[1, 2, 3], [4, 5, 6], [7, 8]], [[3, 2, 1], [6, 5, 4], [8, 7]]),
    ([[23, 40, 10, 34],[34, 10, 40, 23]], [[34, 10, 40, 23],[23, 40, 10, 34]])
])
def test_reverse_lists(arr_x, expected):
    actual = reverse_lists(arr_x)
    assert actual == expected
