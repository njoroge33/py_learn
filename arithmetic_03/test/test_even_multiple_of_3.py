import pytest

from ..even_multiple_of_3 import even_multiple_of_3


@pytest.mark.parametrize('number, expected', [
    (300, True),
    (240, True),
    (16, False),
    (52, False)
])
def test_even_multiple_of_3(number, expected):
    actual = even_multiple_of_3(number)
    assert actual == expected
