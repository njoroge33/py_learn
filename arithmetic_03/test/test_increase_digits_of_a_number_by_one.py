import pytest

from ..increase_digits_of_a_number_by_one import increase_digits_of_a_number_by_one


@pytest.mark.parametrize('number, expected', [
    (299, 410),
    (240, 351),
    (1501, 2612),
    (0, 1)
])
def test_increase_digits_of_a_number_by_one(number, expected):
    actual = increase_digits_of_a_number_by_one(number)
    assert actual == expected
