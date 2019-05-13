from ..fibonacci_series import gen_fib


def test_gen_fib():
	actual = gen_fib(10)
	assert actual == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
