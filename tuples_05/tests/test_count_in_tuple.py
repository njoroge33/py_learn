import pytest
from ..count_in_tuple import get_frequency

@pytest.mark.parametrize('t_tuple, c_n, expected', [
    ((23, 24, 12, 24, 13), 24, 2),
    ((23, 24, 12, 10, 13), 15, 0),
    ((13, 13, 13, 13, 13), 13, 5)
])
def test_get_frequency(t_tuple, c_n, expected):
    actual = get_frequency(t_tuple, c_n)
    assert actual == expected
