import pytest
from ..slicing_tuples import tuple_slice


@pytest.mark.parametrize('names, ages, cities, expected', [
    (('Gitau', 'Kanyoi', 'Ndegwa'), (13, 24, 5), ('Njogu-ini', 'Limuru', 'Kamae'), (
            ('Gitau', 13, 'Njogu-ini'), ('Kanyoi', 24, 'Limuru'), ('Ndegwa', 5, 'Kamae')
    )),
    (('Totua', 'Suhi'), (95, 12, 36, 78), ('Tokyo', 'Vatican', 'Hyderabad'), (
            ('Totua', 95, 'Tokyo'), ('Suhi', 12, 'Vatican')
    )),
])
def test_tuple_slice(names, ages, cities, expected):
    actual = tuple_slice(names, ages, cities)
    assert actual == expected
