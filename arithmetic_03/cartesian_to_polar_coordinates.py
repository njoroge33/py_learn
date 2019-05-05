# Write a program which accepts Cartesian coordinates x and y, and prints its Polar coordinates form
#  i.e. r and Theta (degrees only)
# Round off r and Theta to 2 decimal places
# Program should work for all possible values of x and y (ie, +ve and -ve)
# Info about the procedure to convert Cartesian to Polar co-ordinates could be found here
# http://www.mathsisfun.com/polar-cartesian-coordinates.html
# for more info on this quiz, go to this url: http://www.programmr.com/cartesian-polar-coordinates

import math


def get_quad_offset(x, y):
    x_neg = x < 0
    y_neg = y < 0

    if x_neg and not y_neg:
        return 180
    elif x_neg and y_neg:
        return -180
    elif not x_neg and y_neg:
        return 360
    else:
        return 0


def cartesian_to_polar_coordinates(x, y):
    r = round(math.sqrt(x**2 + y**2), 2)
    theta = get_quad_offset(x, y) + round(math.degrees(math.atan(y/x)), 2)
    return r, theta


if __name__ == "__main__":
    print(cartesian_to_polar_coordinates(12, 5))
