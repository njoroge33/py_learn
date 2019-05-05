import pytest

from ..cartesian_to_polar_coordinates import cartesian_to_polar_coordinates


@pytest.mark.parametrize('x, y, expected', [
    (-3, -4, (5.00, -126.87)),
    (40, 13, (42.06, 18.00)),
    (-33.5, 24, (41.21, 144.38)),
])
def test_cartesian_to_polar_coordinates(x, y, expected):
    actual = cartesian_to_polar_coordinates(x, y)
    assert actual == expected
