import pytest
from ..number_or_not import number_or_not


@pytest.mark.parametrize('num, expected', [
    ('23', 23.0),
    ('there', 'Not a number!')
])
def test_number_or_not(num, expected):
    actual = number_or_not(num)
    assert actual == expected
