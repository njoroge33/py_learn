# Write a Python method countTriplets that accepts a string as an input 
# The method must return the number of triplets in the given string 
# We'll say that a "triplet" in a string is a char appearing three times in a row 
# The triplets may overlap 
# for more info on this quiz, go to this url: http://www.programmr.com/count-triplets


def count_triplets(x_str):
    x_lst = list(x_str)
    count = 0
    prev = ''
    for i in range(len(x_lst) - 1):
        x = x_lst[i]
        y = x_lst[i + 1]
        z = x_lst[i - 1]
        if z == x and x == y and not (z == prev):
            count += 1
            prev = z
        else:
            prev = ''
    return count


if __name__ == "__main__":
    print(count_triplets("jjjjjjkkkohn"))

