import pytest
from ..collatz_sequence import collatz_sequence


@pytest.mark.parametrize('num, expected', [
    (5, [5, 16, 8, 4, 2, 1]),
    (1, [1, 4, 2, 1])
])
def test_collatz_sequence(num, expected):
    actual = collatz_sequence(num)
    assert actual == expected
