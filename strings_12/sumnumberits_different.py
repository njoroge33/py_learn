# Write a Python function that accepts a string as an input 
# The function must return the sum of the digits 0-9 that appear in the string, ignoring all other characters 
# Return 0 if there are no digits in the string 
# for more info on this quiz, go to this url: http://www.programmr.com/sumnumberits-different

import string


def sum_digits(x_str):
    lst = []
    digits = list(string.digits)
    print(digits)
    for i in list(x_str):
        for j in digits:
            if i == j:
                lst.append(i)
    return sum(map(int, lst))


print(sum_digits('hiw33'))
