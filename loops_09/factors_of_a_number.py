# Get the prime factors of a number in the form of a list
# for more info on this quiz, go to this url: http://www.programmr.com/factors-number


def is_prime_number(x):
	if x >= 2:
		for y in range(2, x):
			if not (x % y):
				return False
		return True
	else:
		return False


def prime_factors(x_num):
	fact_lst = []
	try:
		for i in range(2, x_num):
			if x_num % i == 0:
				if is_prime_number(i):
					fact_lst.append(i)
		return fact_lst
	except TypeError:
		return "Wrong data type:X_num expected as an integer"


if __name__ == "__main__":
	print(prime_factors(0))
