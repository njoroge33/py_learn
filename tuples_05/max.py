# using tuples of integers write a function that returns the max of the integers
# for more info on this quiz, go to this url: http://www.programmr.com/max


def tup_max(tup_m):
    maxi = tup_m[0]
    for i in tup_m:
        if i > maxi:
            maxi = i
    return maxi


if __name__ == "__main__":
    print(tup_max((3, 2, 4, 1)))
