import pytest

from ..insertion_at_a_specified_position_in_a_list import insert_into_list


@pytest.mark.parametrize('arr, num, pos, expected', [
    ([0, 2, 5, 6], 10, 2, [0, 2, 10, 5, 6]),
    ([8, 2, 5, 6], 9, 3, [8, 2, 5, 9, 6]),
    ([10, 1, 2, 3, 4, 4], 20, 4, [10, 1, 2, 3, 20, 4, 4])

])
def test_insert_into_list(arr, num, pos, expected):
    actual = insert_into_list(arr, num, pos)
    assert actual == expected
