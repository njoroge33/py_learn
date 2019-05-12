# Write a program to read 3 integer values, a, b, c and then return their sum
# However, if one of the values is the
# same as another of the values, it does not count towards the sum
# for more info on this quiz, go to this url: http://www.programmr.com/unique-sum


def unique_sum(a, b, c):
    original_lst = []
    sec_lst = []
    original_lst.append(a)
    original_lst.append(b)
    original_lst.append(c)
    try:
        for i in original_lst:
            if i not in sec_lst:
                sec_lst.append(i)
        return sum(sec_lst)
    except TypeError:
        return "Wrong data type! Integers expected"


print(unique_sum(3, 3, 3))
