# Write a program to check whether a number given by the user is EVEN or ODD ?
# If Even return EVEN and if ODD, return ODD
# for more info on this quiz, go to this url: http://www.programmr.com/evens-and-odds-2


def is_even_or_odd(num):
    try:
        if num % 2 == 0:
            return "EVEN"
        return "ODD"
    except TypeError:
        return "Wrong data type!: you are expected to enter an integer"


if __name__ == "__main__":
    print(is_even_or_odd(9))
