# Given an array X[0...n-1] of integers
# Sort the array in ascending order first
# Then find an array element such that X[i] = i, i.e. the value of element at index i is equal to i
# Return the value or None if there isn't such an element
# for more info on this quiz, go to this url: http://www.programmr.com/find-if-index-and-element-are-equal


def index_and_element_equal(x_arr):
    x_arr.sort()
    for i in x_arr:
        if i == x_arr[i]:
            print(i)
        else:
            return "None"


if __name__ == "__main__":
    print(index_and_element_equal([3, 5, 6, 7, 8, 0, 2, 1]))
