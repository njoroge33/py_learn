# Sexy Pairs are nothing but those pairs which contain prime numbers with a difference of 6
# Consider 5, it is a prime no
# and adding 6 to 5 makes 11 which is also a prime no
# So (5,11) is a sexy pair
# Write a program which calculates Sexy pairs up to the limit given as input
# for more info on this quiz, go to this url: http://www.programmr.com/sexy-pair


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
        return True
    else:
        return False


def get_sexy_pairs(limit):
    lst = []
    for i in range(limit):
        if is_prime_number(i) and is_prime_number(i + 6):
            if i + 6 < limit:
                lst.append((i, i+6))
    return lst


if __name__ == "__main__":
    print(get_sexy_pairs(20))
