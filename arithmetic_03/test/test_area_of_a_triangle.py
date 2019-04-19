import pytest

from ..area_of_triangle import area_triangle


@pytest.mark.parametrize('a, b, c, expected', [
    (23, 45, 67, 183.8265),
    (3, 4, 3, 4.4721),
    (8, 44, 41, 156.8946)
])
def test_area_triangle(a, b, c, expected):
    actual = area_triangle(a, b, c)
    assert actual == expected
