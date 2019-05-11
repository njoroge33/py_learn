# Write a function py_sort that takes a list of integers and returns the list with its
# members arranged in ascending order
# Example:
# Given [3, 1, 56, 12, 34, 57] return [1, 3, 12, 34, 56, 57]
# for more info on this quiz, go to this url: http://www.programmr.com/ascending-order


def py_sort(x_arr):
    try:
        for i in range(len(x_arr)):
            for j in range(i+1, len(x_arr)):
                if x_arr[i] > x_arr[j]:
                    temp = x_arr[i]
                    x_arr[i] = x_arr[j]
                    x_arr[j] = temp
        return x_arr
    except TypeError:
        return "Only supports a list"


if __name__ == "__main__":
    print(py_sort([3, 6, 4, 1]))
