# Write a code to check the input given by the user as follows
# Input: 5 Output: 5.0
# Input: abc Output: Not a number!
# for more info on this quiz, go to this url: http://www.programmr.com/number-or-not


def number_or_not(num):
    try:
        return float(num)
    except ValueError:
        return "Not a number!"


print(number_or_not("abc"))
