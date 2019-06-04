# Find if an alphabet is present in a string  or not and
# if yes then print its position and  count how many times it present
# for more info on this quiz, go to this url: http://www.programmr.com/find-alphabet-and-count-it


def alphabet_count(x_string, alphabet):
    lst = []
    count = 0
    for i in range(len(x_string)):
        if x_string[i] == alphabet:
            lst.append(i)
            count += 1
    if count == 0:
        return False
    lst.append(count)
    return tuple(lst)


print(alphabet_count("yhffhf", "o"))
