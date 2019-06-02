# Write a recursive function to print the factorial of a number 
# A recursive function is one which calls itself
# for more info on this quiz, go to this url: http://www.programmr.com/recursive-functions


def fact(num):
    if num < 1:
        return 1
    return num * fact(num - 1)


if __name__ == "__main__":
    print(fact(1))
