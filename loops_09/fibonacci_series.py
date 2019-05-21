# Write a program to print the fibonacci series till the limit n
# return the series in a list
# for more info on this quiz, go to this url: http://www.programmr.com/fibonacci-series


def gen_fib(n):
	lst = []
	first = 0
	second = 1
	try:
		for i in range(n + 1):
			lst.append(first)
			temp = first
			first = second
			second = temp + second
		return lst
	except TypeError:
		return "Wrong data type:n expected as an integer"


if __name__ == "__main__":
	print(gen_fib(10))
