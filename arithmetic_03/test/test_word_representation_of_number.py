import pytest

from ..word_representation_of_a_number import word_rep_of_number


@pytest.mark.parametrize('number, expected', [
    (12, 'twelve'),
    (201, 'two hundred and one'),
    (3, 'three'),
    (600, 'six hundred '),
    (601, 'six hundred and one'),
    (310, 'three hundred and ten'),
    (10, 'ten')
])
def test_get_sexy_pairs(number, expected):
    actual = word_rep_of_number(number)
    assert actual == expected
