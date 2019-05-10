import pytest
from ..right_angled_triangle import is_right_angled_triangle


@pytest.mark.parametrize('a, b, c, expected', [
    (2, 2, 2, False),
    (4, 5, 3, True),
    (12, 5, 13, True),
    (40, 41, 9, True),
    (30, 80, 20, False)
])
def test_is_right_angled_triangle(a, b, c, expected):
    actual = is_right_angled_triangle(a, b, c)
    assert actual == expected
