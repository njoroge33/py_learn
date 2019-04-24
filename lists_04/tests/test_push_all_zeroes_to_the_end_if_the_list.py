import pytest

from ..push_all_zeros_to_the_end_of_the_list import zeroes_to_end


@pytest.mark.parametrize('arr_x, expected', [
    ([2, 0, 3, 0, 5, 6, 0, 7, 3], [2, 3, 5, 6, 7, 3, 0, 0, 0]),
    ([0, 3, 10, 23, 40, 10, 0], [3, 10, 23, 40, 10, 0, 0]),
    ([2, 3, 11, 23, 40, 10, 34], [2, 3, 11, 23, 40, 10, 34]),
    ([0, 0, 0], [0, 0, 0])
])
def test_zeroes_to_end(arr_x, expected):
    actual = zeroes_to_end(arr_x)
    assert actual == expected
