import pytest
from ..angle_pairs import angle_pairs


@pytest.mark.parametrize("a, b, c, expected", [
    (30, 40, 50, False),
    (105, 15, 75, True),
    (90, 40, 90, False)
])
def test_angle_pairs(a, b, c, expected):
    actual = angle_pairs(a, b, c)
    assert actual == expected
