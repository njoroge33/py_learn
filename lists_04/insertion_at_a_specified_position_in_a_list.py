# Given a list x of length n, a number to be inserted into the list and a position where to insert the number
# return the new list
# e.g given [2, 3, 6, 7], num=8 and position=2, return [2, 3, 8, 6, 7]
# for more info on this quiz, go to this url: http://www.programmr.com/insertion-specified-position-array-0


def insert_into_list(arr, num, position):
    b = arr[:position] + [num] + arr[position:]
    return b


if __name__ == "__main__":
    print(insert_into_list([1, 2, 3, 4], 5, 4))
