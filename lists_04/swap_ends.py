# Given an array of integers
# Swap the first element and the last element in the array
# return the modified array
# The array length should be at least 1
# for more info on this quiz, go to this url: http://www.programmr.com/swap-ends-1


def swap_ends(arr_x):
    a = []
    for i in range(len(arr_x), len(arr_x)+1):
        a.append(i)
    for i in range(2, len(arr_x)):
        a.append(i)
    for i in range(1, 2):
        a.append(i)
    print(a)


if __name__ == "__main__":
    print(swap_ends([1, 2, 3, 4, 5]))
