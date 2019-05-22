# Write a function which takes as string and a character as parameters, and displays the string with all occurrences
# of the character removed from it
# for more info on this quiz, go to this url: http://www.programmr.com/remove-character-0


def remove_char(x_string, char):
    y_list = []
    for i in x_string:
        if i != char:
            y_list.append(i)
    return "".join(y_list)


if __name__ == "__main__":
    print(remove_char("teudsf", "d"))
