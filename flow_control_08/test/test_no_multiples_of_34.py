import pytest
from ..no_multiples_of_34 import remove_mult_of_3_and_4


@pytest.mark.parametrize('num, expected', [
    (4, [0, 1, 2]),
    (10, [0, 1, 2, 5, 6, 7, 9, 10]),
    (0, [0])
])
def test_remove_mult_of_3_and_4(num, expected):
    actual = remove_mult_of_3_and_4(num)
    assert actual == expected
