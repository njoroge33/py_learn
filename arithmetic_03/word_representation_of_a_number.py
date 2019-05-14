# Write a program to turn a number into its English name
# Assume that the number is positive below 1000
# for more info on this quiz, go to this url: http://www.programmr.com/word-representation-number


ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decade = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def first(num):
    for i in num:
        if num[0] == i:
            return ones[i] + " " + "hundred"


def three_numb(num):
    for i in num:
        if num[1] == 0 and num[2] == 0:
            return""
        elif num[1] == 0 and num[2] == i:
            return "and" + " " + ones[i]
        elif num[1] == i and num[2] == 0:
            return "and" + " " + decade[i]
        elif num[1] == 1 and num[2] == i:
            return "and" + " " + teens[i]
        elif num[1] > 1 and num[2] == i:
            return "and" + " " + decade[num[1]] + " " + ones[i]


def two_numb(num):
    for i in num:
        if num[0] == i and num[1] == 0:
            return decade[i]
        elif num[0] == 1 and num[1] == i:
            return teens[i]
        elif num[0] > 1 and num[1] == i:
            return decade[num[0]] + " " + ones[i]


def single_numb(num):
    for i in num:
        return ones[i]


def word_rep_of_number(number):
    num = list(map(int, str(number)))
    if len(num) == 3:
        return first(num) + " " + three_numb(num)
    elif len(num) == 2:
        return two_numb(num)
    elif len(num) == 1:
        return single_numb(num)


if __name__ == "__main__":
    print(word_rep_of_number(310))
