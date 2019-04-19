# Print the remainder of a/b. Make sure that b is not zero. If b is zero, display corresponding error message.
# Otherwise, display the result of remainder operation.
# Enter the 1st number:2
# Enter the 2nd number:4
# Remainder is: 2
# for more info on this quiz, go to this url: http://www.programmr.com/modulus-variables-0


def modulus(a, b):
    if b == 0:
        return "Math error"
    else:
        return a % b


if __name__ == "__main__":
    print(modulus(2, 4))
