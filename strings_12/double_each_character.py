# Given a string, return a string where for every character in the original string, there are two characters 
# for more info on this quiz, go to this url: http://www.programmr.com/double-each-character


def double_char(x_str):
    a = []
    for i in x_str:
        a.append(i * 2)
    return "".join(a)


if __name__ == "__main__":
    print(double_char("abb"))
