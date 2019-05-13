# Take any natural number n
# If n is even, divide it by 2 to get n / 2
# If n is odd, multiply it by 3 and add 1 to get 3n + 1
# Repeat the process indefinitely
# In 1937, Lothar Collatz proposed that no matter what number you begin with, the sequence eventually reaches 1
# This is widely believed to be true, but has never been formally proved
# Write a function that takes a number and then returns the Collatz Sequence starting from that number
# Stop when you reach 1
# return the number of steps and Collatz Sequence
# Example: given 1 return ([5, 16, 8, 4, 2, 1], 5)
# for more info on this quiz, go to this url: http://www.programmr.com/collatz-sequence-4


class ZeroError(Exception):
    pass


def collatz_sequence(num):
    if num == 0:
        raise ZeroError("number less than 1")
    sequence = [num]
    stop = False
    while not stop:
        if num % 2 == 0:
            num = num // 2
            sequence.append(num)
        else:
            num = num * 3 + 1
            sequence.append(num)
        if num == 1:
            stop = True
    return sequence


if __name__ == '__main__':
    print(collatz_sequence(0))
