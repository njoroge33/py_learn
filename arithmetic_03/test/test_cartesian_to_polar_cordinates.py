import pytest

from ..cartesian_to_polar_coordinates import cartesian_to_polar_coordinates


@pytest.mark.parametrize('x, y, expected', [
    (12, 5, (13.00, 67.38)),
    (-3, -4, (5.00, 36.87)),
    (40, 13, (42.06, 72.0)),
    (-33.5, 24, (41.21, -54.38)),
])
def test_cartesian_to_polar_coordinates(x, y, expected):
    actual = cartesian_to_polar_coordinates(x, y)
    assert actual == expected
