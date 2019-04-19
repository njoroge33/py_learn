import pytest

from ..cartesian_to_polar_coordinates import cartesian_to_polar_coordinates


@pytest.mark.parametrize('x, y, expected', [
    (12, 5, (13.00, 22.6)),
    (-3, -4, (5.00, -126.86)),
    (40, 13, (42.05, 18.00)),
    (-33.5, 24, (41.20, 144.38)),
])
def test_cartesian_to_polar_coordinates(x, y, expected):
    actual = cartesian_to_polar_coordinates(x, y)
    assert actual == expected
