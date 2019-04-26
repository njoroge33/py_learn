# Write a method named swapPairs that accepts a list of strings as a parameter and
#  switches the order of values in a pairwise fashion
# Your method should switch the order of the first two values, then switch the order of the next two,
#  switch the order of the next two, and so on
# for more info on this quiz, go to this url: http://www.programmr.com/swappairs


def swap_pairs(arr_x):
    b = []
    c = []
    for i in range(len(arr_x)-1):
        b.append([arr_x[i], arr_x[i+1]])
    print(b)
    for i in reversed(b):
        c.append(i)
    print(c)


if __name__ == "__main__":
    swap_pairs([5, 7, 11, 4, 5])
