# Find the LCM of two numbers
# for more info on this quiz, go to this url: http://www.programmr.com/find-lcm


def lcm(m, n):
	large = max(m, n)
	small = min(m, n)
	i = large
	try:
		while True:
			if i % small == 0:
				return i
			i += large
	except TypeError:
		return "Wrong data type"


if __name__ == "__main__":
	print(lcm(7, 5))
