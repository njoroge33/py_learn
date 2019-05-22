# Write a function NumberOfChar(str),that takes in a string and returns the number of characters in that string ?
# for more info on this quiz, go to this url: http://www.programmr.com/number-characters


def number_of_char(x_str):
	count = 0
	for i in x_str:
		count += 1
	return count


if __name__ == "__main__":
	print(number_of_char("hheg dhdh"))
