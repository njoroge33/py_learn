# Write a program which determines whether a given string is palindrome or not 
# for more info on this quiz, go to this url: http://www.programmr.com/palindrome-string-2


def palindrome(x_string):
    if x_string[0::] == x_string[::-1]:
        return True
    return False


if __name__ == "__main__":
    print(palindrome("aka"))
