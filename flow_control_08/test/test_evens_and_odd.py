import pytest
from ..evens_and_odds import is_even_or_odd


@pytest.mark.parametrize('a, b, c, expected', [
    (10, 'EVEN'),
    (51, 'ODD'),
    (0, 'EVEN')
])
def test_is_even_or_odd(a, b, c, expected):
    actual = is_even_or_odd(a, b, c)
    assert actual == expected


def test_is_even_or_odd_raises_error_value_error():
    with pytest.raises(ValueError) as err:
        is_even_or_odd('NOT A NUMBER')
        assert err


def test_is_even_or_odd_raises_error_zero_division_error():
    with pytest.raises(ZeroDivisionError) as err:
        is_even_or_odd(0)
        assert err
