import pytest
from ..basic_nested_loops import gen_coordinates


@pytest.mark.parametrize('x_num, expected', [
	(2, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
])
def test_gen_coordinates(x_num, expected):
	actual = gen_coordinates(x_num)
	assert actual == expected
