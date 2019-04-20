# Write a program to check whether a number is an even multiple of 3
# for more info on this quiz, go to this url: http://www.programmr.com/even-multiple-3


def even_multiple_of_3(number):
    if number % 3 == 0 and number % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(even_multiple_of_3(6))
