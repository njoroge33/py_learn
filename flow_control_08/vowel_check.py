# Write a program which takes a string as an input and prints the string without the vowels
# for more info on this quiz, go to this url: http://www.programmr.com/vowel-check


def remove_vowels(x_str):
    y_str = []
    lst = list("aeiouAEIOU")
    try:
        for i in x_str:
            if i not in lst:
                y_str.append(i)
        return "".join(y_str)
    except TypeError:
        return "Wrong data type! string expected"


print(remove_vowels("johnGICHUHI"))
