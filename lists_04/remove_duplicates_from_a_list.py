# Write a program that accepts a list of elements from the user and
#  then print the list after removing all duplicate values, preserving the original order
# for more info on this quiz, go to this url: http://www.programmr.com/remove-duplicates-list


def remove_duplicates(arr_x):
    a = []
    for i in arr_x:
        if i not in a:
            a.append(i)
    return a


print(remove_duplicates([1, 2, 5, 5, 3, 3, 7, 3]))
