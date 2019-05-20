import pytest
from ..sum_of_numbers_in_a_string import sum_numbers


@pytest.mark.parametrize('x_str, expected', [
	('wha7 1s 5h71s', 21),
	('what is this', 0)
])
def test_sum_numbers(x_str, expected):
	actual = sum_numbers(x_str)
	assert actual == expected
