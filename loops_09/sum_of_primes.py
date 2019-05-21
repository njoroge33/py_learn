# Write a program to calculate the sum of all prime numbers from 1 till n
# for more info on this quiz, go to this url: http://www.programmr.com/sum-primes


class ZeroError(Exception):
	pass


def is_prime_number(x):
	if x >= 2:
		for y in range(2, x):
			if not (x % y):
				return False
		return True
	else:
		return False


def sum_of_primes(num):
	lst = []
	try:
		if num <= 1:
			raise ZeroError(" ")

		for i in range(num+1):
			if is_prime_number(i):
				lst.append(i)
		return sum(lst)
	except Exception:
		return "Limit should start from two and should be an integer"


if __name__ == "__main__":
	print(sum_of_primes(2))
