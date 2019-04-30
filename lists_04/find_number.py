# Write a program that takes a list of numbers, and a number to search for
# If the number is in the list return its index
# If it isn't, return None
# for more info on this quiz, go to this url: http://www.programmr.com/find-number-0


def find_number(x_arr, x):
    for i in x_arr:
        if x == i:
            return x_arr.index(x)
    else:
            return None


if __name__ == "__main__":
    print(find_number([1, 2, 3, 4, 6], 8))
