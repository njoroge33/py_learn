# Write a simple program that to check whether is leap year or not from user input
# guide for leap years rules: https://www.cs.usfca.edu/~cruse/cs210s07/leapyear.bob
# for more info on this quiz, go to this url: http://www.programmr.com/leap-year-5


def is_leap_year(year):
    try:
        if year % 4 == 0:
            return True
        return False
    except TypeError:
        return "Wrong data type!: year expected as an integer"


if __name__ == "__main__":
    print(is_leap_year(1998))
