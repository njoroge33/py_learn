# Take two numbers from user and pass them to a method which will return their GCD 
# for more info on this quiz, go to this url: http://www.programmr.com/greatest-common-divisor-3


def greatest_divisor(num_1, num_2):
    if num_1 > num_2:
        small = num_2
    else:
        small = num_1

    for i in range(1, small + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd = i
    return gcd


if __name__ == "main":
    print(greatest_divisor(12, 16))
