# Write a program to swap adjacent elements in an array 
# Assume that array size is at least 1 
# for more info on this quiz, go to this url: http://www.programmr.com/swapping-adjacent-elements


def swap_adjacent(arr_x):
    b = []
    for i in range(len(arr_x)-1):
        b.append((arr_x[i + 1], arr_x[i]))
    print(list(b))


if __name__ == "__main__":
    swap_adjacent([1, 2, 3, 4])
