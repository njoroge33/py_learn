import pytest

from ..average_and_percentage import average


@pytest.mark.parametrize('a, b, c, d, expected', [
    (10, 10, 10, 10, 10),
    (20, 20, 20, 20, 20),
    (100, 100, 100, 100, 100)
])
def test_area_average(a, b, c, d, expected):
    actual = average(a, b, c, d)
    assert actual == expected
