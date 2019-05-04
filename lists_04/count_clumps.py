# Say that a "clump" in an array is a series of 2 or more adjacent elements of the same value
# Return the number of clumps in the given array
# for more info on this quiz, go to this url: http://www.programmr.com/count-clumps-3


def count_clumps(x_arr):
    count = 0
    prev = ''
    for i in range(len(x_arr)-1):
        x = x_arr[i]
        y = x_arr[i+1]
        if x == y and not(x == prev):
            count += 1
            prev = x
        elif y == prev:
            prev = y
        else:
            prev = ''
    return count


if __name__ == "__main__":
    print(count_clumps([1, 1, 1, 1, 1, 1]))
