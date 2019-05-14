import pytest
from ..factors_of_a_number import prime_factors


@pytest.mark.parametrize('x_num, expected', [
	(10, [2, 5]),
	(150, [2, 3, 5, 5]),
	(30, [2, 3, 5]),
	(0, [])
])
def test_gen_coordinates(x_num, expected):
	actual = prime_factors(x_num)
	assert actual == expected
