import pytest
from ..ascending_order import py_sort


@pytest.mark.parametrize('x_arr, expected', [
    ([3, 1, 56, 12, 34, 57], [1, 3, 12, 34, 56, 57]),
    ([3], [3]),
    ([-23, -45, -41, 4, 12, 4], [-45, -41, -23, 4, 4, 12])
])
def test_py_sort(x_arr, expected):
    actual = py_sort(x_arr)
    assert actual == expected
