# Write a program that takes a list of numbers, and a number to search for
# If the number is in the list return its index
# If it isn't, return None
# for more info on this quiz, go to this url: http://www.programmr.com/find-number-0


def find_number(x_arr, x):
    if x not in x_arr:
        return "None"
    else:
        return x_arr.index(x)


if __name__ == "__main__":
    print(find_number([1, 2, 3, 4, 6], 6))
