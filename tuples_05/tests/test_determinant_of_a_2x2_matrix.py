import pytest
from ..determinant_of_a_2x2_matrix import determinant

@pytest.mark.parametrize('tuple_x, tuple_y, expected', [
    ((23, 13), (8, 6), 34),
    ((3, 8), (4, 6), -14),
    ((4, 6), (3, 8), 14)
])
def test_determinant(tuple_x, tuple_y, expected):
    actual = determinant(tuple_x, tuple_y)
    assert actual == expected
