# In this exercise, complete the function that "returns a value"
# When you call this function, it should calculate the area of the triangle using Heron's formula and return it
# Heron's formula:
#      Area = √(s*(s-a)*(s-b)*(s-c))
# 5 where s = (a+b+c)/2
# result should be to 4 decimal places
# for more info on this quiz, go to this url: http://www.programmr.com/area-triangle-0
from math import sqrt


def area_triangle(a, b, c):
    s = (a + b + c)/2
    area = sqrt(s * (s - a)*(s - b)*(s - c))
    return round(area, 4)


if __name__ == "__main__":
    print(area_triangle(6, 4, 8))

