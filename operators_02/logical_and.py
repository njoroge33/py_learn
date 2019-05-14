# Write a progam that performs Logical AND operation on two numbers
# for more info on this quiz, go to this url: http://www.programmr.com/logical-and-2


def logical_and(a, b):
    return bin(a & b)


if __name__ == "__main__":
    print(logical_and(14, 5))
