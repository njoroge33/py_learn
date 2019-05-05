# write a function that takes a list of lists
# Each list has 5 numbers
# reverse each list in the big list but maintain the order of the lists
# e.g given [[1, 2, 3], [4, 5, 6], [7, 8]] return [[3, 2, 1], [6, 5, 4], [8, 7]]
# for more info on this quiz, go to this url: http://www.programmr.com/reverse-lists


def reverse_lists(arr_y):
    rev_lst = []
    for i in arr_y:
        i.reverse()
        rev_lst.append(i)
    return rev_lst


print(reverse_lists([[1, 2, 3], [4, 5, 6], [7, 8]]))
