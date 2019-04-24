# Write a program to check if a number is Perfect or not
# A perfect number is a positive integer that is the sum of its proper positive divisors excluding the number itself
# for more info on this quiz, go to this url: http://www.programmr.com/perfect-number-3


def is_perfect(number):
    new_lst = []
    for i in range(1, number):
        if number % i == 0:
            new_lst.append(i)
    print(new_lst)
    if sum(new_lst) == number:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_perfect(14))
