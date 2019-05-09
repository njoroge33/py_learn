# using tuples of integers write a function that returns the min of the integers
# for more info on this quiz, go to this url: http://www.programmr.com/min


def tup_min(tup_n):
    mini = tup_n[0]
    for i in tup_n:
        if i < mini:
            mini = i
    return mini


if __name__ == "__main__":
    print(tup_min((3, 2, 4, 1)))
