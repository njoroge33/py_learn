import pytest

from ..perfect_number import is_perfect


@pytest.mark.parametrize('number, expected', [
    (6, True),
    (14, False),
    (-1501, False),
    (678, False),
    (28, True)
])
def test_is_perfect(number, expected):
    actual = is_perfect(number)
    assert actual == expected
