# Write a function length(str), which takes in a string,
# and raises an exception - LengthError if length of the string is less than 3 and prints the length otherwise?
# for more info on this quiz, go to this url: http://www.programmr.com/raising-exceptions

# This is how we create custom Exceptions


class LengthError(Exception):
    pass


def length(x_str):
    if len(x_str) < 3:
        raise LengthError("String too short")
    return len(x_str)


if __name__ == "__main__":
    print(length("dI"))
