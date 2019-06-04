# Write a program which takes in a string and count the number of occurrence of a character chosen by the user
# for more info on this quiz, go to this url: http://www.programmr.com/count-character


def count_char(x_str, char):
    count = 0
    for i in list(x_str):
        if char == i:
            count += 1
    return count


if __name__ == "__main__":
    print(count_char("johno", "o"))
