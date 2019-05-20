# Write a method that rotates the elements of a list by a given factor d i.e.
# moving the elements of the list to left by d, like this:
# Original List: [1 2 3 4 5 6 7], After rotating by a factor of 2 : [3 4 5 6 7 1 2]
# for more info on this quiz, go to this url: http://www.programmr.com/rotate-list


def rotate_list(arr_x, factor):
    rotate_lst = []
    for i in range(factor + 1, len(arr_x) + 1):
            rotate_lst.append(i)
    for i in range(1, factor + 1):
            rotate_lst.append(i)
    print(rotate_lst)


if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5, 6, 7], 2))
