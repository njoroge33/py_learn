import pytest
from ..vowel_check import remove_vowels


@pytest.mark.parametrize('x_str, expected', [
    ('githeri', 'gthr'),
    ('alphabet', 'lphbt'),
    ('we went to glasgow', 'w wnt t glsgw'),
    ('karoboshter demakufu', 'krbshtr dmkf')
])
def test__remove_vowels(x_str, expected):
    actual = remove_vowels(x_str)
    assert actual == expected
