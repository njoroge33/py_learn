import pytest
from ..evens_and_odds import is_even_or_odd


@pytest.mark.parametrize('a, expected', [
    (10, 'EVEN'),
    (51, 'ODD'),
    (0, 'EVEN')
])
def test_is_even_or_odd(a, expected):
    actual = is_even_or_odd(a)
    assert actual == expected
