# Write a function fact() to find the factorial of a given number
# for more info on this quiz, go to this url: http://www.programmr.com/factorial-number-3


def fact(n):
	total = 1
	try:
		for i in range(1, n+1):
			total = total * i
		return total
	except TypeError:
		return "Wrong data type: n expected as an integer"


if __name__ == "__main__":
	print(fact(6))
