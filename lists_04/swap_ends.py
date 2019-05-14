# Given an array of integers
# Swap the first element and the last element in the array
# return the modified array
# The array length should be at least 1
# for more info on this quiz, go to this url: http://www.programmr.com/swap-ends-1


def swap_ends(arr_x):

    arr_x[0], arr_x[-1] = arr_x[-1], arr_x[0]

    return arr_x


if __name__ == "__main__":
    print(swap_ends([2, 3, 3, 4, 5]))
