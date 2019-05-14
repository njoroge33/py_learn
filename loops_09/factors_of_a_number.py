# Get the prime factors of a number in the form of a list
# for more info on this quiz, go to this url: http://www.programmr.com/factors-number


def prime_factors(x_num):
	fact_lst = []
	try:
		for i in range(2, x_num):
			if x_num % i == 0:
				fact_lst.append(i)
		return fact_lst
	except TypeError:
		return "Wrong data type:X_num expected as an integer"


if __name__ == "__main__":
	print(prime_factors(30))
