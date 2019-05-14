import pytest
from ..substring_occurrences_as_a_tuple import occurrences


@pytest.mark.parametrize('s_str, k_str, expected', [
    ('tattattata', 'tt', (2, 5)),
    ('sesasesu', 'sb', None),
    ('sesasesu', 'es', (1, 5))
])
def test_occurrences(s_str, k_str, expected):
    actual = occurrences(s_str, k_str)
    assert actual == expected
