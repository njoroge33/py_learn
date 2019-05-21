# Write a Python function sumNumbers() that accepts a string as an input
# The function must return the sum of the numbers appearing in the string, ignoring all other characters
# for more info on this quiz, go to this url: http://www.programmr.com/sum-numbers-string


def sum_numbers(x_str):
    y_str = []
    lst = list("1234567890")
    try:
        for i in x_str:
            if i in lst:
                y_str.append(i)
        return sum(map(int, y_str))
    except TypeError:
        return "Wrong data type! string expected"


if __name__ == "__main__":
    print(sum_numbers("k566am877"))
