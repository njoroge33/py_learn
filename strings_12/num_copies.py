# Given a string and a non-negative int n, return a larger string that is n copies of the original string 
# for more info on this quiz, go to this url: http://www.programmr.com/n-copies-original-string


def num_copies(x_string, num):
    return x_string * num


if __name__ == "__main__":
    print(num_copies("aa", 2))
