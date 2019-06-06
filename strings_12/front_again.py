# Given a string with length > 1, return true if the first 2 chars in the string also appear at the end of the string
#  (ignore case)
# for more info on this quiz, go to this url: http://www.programmr.com/front-again-2


def front_end(x_str):
    if len(x_str) > 1:
        if x_str[:2] == x_str[-2:]:
            return True
        return False
    return False


if __name__ == "__main__":
    print(front_end("edited"))
