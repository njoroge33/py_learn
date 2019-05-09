# Write a program that takes a tuple of integers and a number to count,
#  and returns the number of times that number appears in the tuple
# If the number isn't in the tuple, you should return 0
# for more info on this quiz, go to this url: http://www.programmr.com/count-tuple


def get_frequency(tup_x, n_to_count):
    count = 0
    for i in tup_x:
        if i == n_to_count:
            count += 1
    return count


if __name__ == "__main__":
    print(get_frequency((23, 24, 12, 24, 13), 24))
