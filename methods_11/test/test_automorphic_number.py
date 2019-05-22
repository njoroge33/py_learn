import pytest
from ..automorphic_number import auto_number


@pytest.mark.parametrize("number, expected", [
    (4, False),
    (5, True),
    (67, False),
    (76, True),
    (890625, True)

])
def test_automorphic_number(number, expected):
    actual = auto_number(number)
    assert actual == expected
