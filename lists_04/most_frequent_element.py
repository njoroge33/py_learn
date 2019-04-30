# Write a program to find the most popular element in an array
# Assume that array size is at least 1
# return None if there ain't any
# for more info on this quiz, go to this url: http://www.programmr.com/most-frequent-element-1


def find_popular_item(arr_x):
        counter = 0
        num = arr_x[0]
        if len(arr_x) == 1:
            return num

        for i in arr_x:
            curr_frequency = arr_x.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i

        if counter <= 1:
            return None
        else:
            return num


if __name__ == "__main__":
    print(find_popular_item([2]))
