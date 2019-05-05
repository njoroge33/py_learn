# Write a method called allLess that accepts two lists of integers and
# returns true if each element in the first list is less than the element at the same index in the second list
# Your method should return false if the lists are not of same length
# for more info on this quiz, go to this url: http://www.programmr.com/allless


def all_less(x_list, y_list):
    if len(x_list) != len(y_list):
        return False

    for i in range(len(x_list)):
        if y_list[i] - x_list[i] < 0:
            return False

    return True


if __name__ == "__main__":
    print(all_less([1, 2, 3, 4], [5, 1, 7, 8]))
