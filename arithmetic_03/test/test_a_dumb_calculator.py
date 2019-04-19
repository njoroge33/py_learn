import pytest

from ..a_dumb_calculator import calculator


@pytest.mark.parametrize('a, b, c, expected', [
    (12, 34, 4, 25.0),
    (30, 30, 30, 45.0),
    (12, 26, 3, 20.5)
])
def test_calculator(a, b, c, expected):
    actual = calculator(a, b, c)
    assert actual == expected
