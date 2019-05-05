# Given a list of length > 1, return the list with its items in the reverse order,
# do not use list reverse methods like .reverse or [::-1]
# for more info on this quiz, go to this url: http://www.programmr.com/reverse-list


def reverse_list(arr_x):
    new_lst = []
    b = len(arr_x)-1
    for i in range(len(arr_x)):
        while b >= 0:
            new_lst.append(arr_x[b])

            b -= 1
    return new_lst


print(reverse_list([1, 2, 3, 4, 5, 6, 7]))
