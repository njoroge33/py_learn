# Use some simple nested for loops to generate all possible coordinates from (0,0) up to given number
# Output should be as shown below
# for more info on this quiz, go to this url: http://www.programmr.com/basic-nested-loops-6


def gen_coordinates(x_num):
	x_lst = []
	try:
		for x in range(x_num + 1):
			for y in range(x_num + 1):
				x_lst.append((x, y))
		return x_lst
	except TypeError:
		return "Wrong data type"


if __name__ == "__main__":
	print(gen_coordinates(5))
