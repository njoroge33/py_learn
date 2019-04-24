# Write a program to find the root of a number n to the power 1/x where x and n are the numbers input by the user
# example n = 10000, x = 4 root = 10
# for more info on this quiz, go to this url: http://www.programmr.com/roots


def get_root(x, n):
    return n ** (1/x)


if __name__ == "__main__":
    print(get_root(5, 32))
