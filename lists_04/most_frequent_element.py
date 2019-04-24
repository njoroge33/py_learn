# Write a program to find the most popular element in an array
# Assume that array size is at least 1
# return None if there ain't any
# for more info on this quiz, go to this url: http://www.programmr.com/most-frequent-element-1


def find_popular_item(arr_x):
    return max(set(arr_x), key=arr_x.count)


if __name__ == "__main__":
    print(find_popular_item([1, 2, 5, 5, 3, 3, 7, 3]))
