# Write a program which takes 3 int values and checks if any of their combinations
# can form the sides of a right angled triangle or not
# return a True or False
# for more info on this quiz, go to this url: http://www.programmr.com/right-angled-triangle


def is_right_angled_triangle(a, b, c):
    try:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
        return False
    except TypeError:
        return "Wrong data type! Integers expected"


if __name__ == "__main__":
    print(is_right_angled_triangle(4, 9, 3))
