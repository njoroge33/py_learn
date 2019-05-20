import pytest
from ..factorial_of_a_number import fact


@pytest.mark.parametrize('x_num, expected', [
	(5, 120),
	(6, 720),
	(0, 1)
])
def test_fact(x_num, expected):
	actual = fact(x_num)
	assert actual == expected
