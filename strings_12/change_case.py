# User enters a string in mixed case(uppercase +lowercase),
# code so that uppercase is changed to lowercase and vice-versa
# for more info on this quiz, go to this url: http://www.programmr.com/change-case-2


import string


def change_case(x_str):
    a = {char: char for char in list(string.ascii_lowercase)}
    b = {chr: chr for chr in list(string.ascii_uppercase)}

    x_str_lst = list(x_str)
    for i, c in enumerate(x_str_lst):
        if a.get(c):
            x_str_lst[i] = c.upper()
        elif b.get(c):
            x_str_lst[i] = c.lower()

    return ''.join(x_str_lst)


if __name__ == "__main__":
    print(change_case("jOhN"))
