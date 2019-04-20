import pytest

from ..cartesian_to_polar_coordinates import cartesian_to_polar_coordinates


@pytest.mark.parametrize('x, y, expected', [
    (12, 5, (13.00, 22.62)),
    (-3, -4, (5.00, 53.13)),
    (40, 13, (42.06, 18.0)),
    (-33.5, 24, (41.21, -35.62)),
])
def test_cartesian_to_polar_coordinates(x, y, expected):
    actual = cartesian_to_polar_coordinates(x, y)
    assert actual == expected
