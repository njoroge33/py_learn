import pytest
from ..find_lcm import lcm


@pytest.mark.parametrize('m, n, expected', [
	(20, 30, 60),
	(23, 12, 276),
	(70, 14, 70),
	(20, 15, 60),
])
def test_gen_coordinates(m, n, expected):
	actual = lcm(m, n)
	assert actual == expected
