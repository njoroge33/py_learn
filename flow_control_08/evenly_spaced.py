# Given three ints, a b c, one of them is small, one is medium and one is large.
# Return true if the three values are evenly spaced,
# Evenly spaced means that:
# the difference between small and medium is the same as the difference between medium and large.
#
# for more info on this quiz, go to this url: http://www.programmr.com/evenly-spaced-1


def evenly_spaced(a, b, c):
    try:
        if b - a == c - b:
            return True
        return False
    except TypeError:
        return "Wrong data type!"


print(evenly_spaced(1, 3, 5))
