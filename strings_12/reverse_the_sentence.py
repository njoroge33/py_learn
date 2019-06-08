# Write a program to reverse the sentence wordwise 
# for more info on this quiz, go to this url: http://www.programmr.com/reverse-sentence


def reverse_str(x_str):
    x_lst = x_str.split(" ")
    return" ".join(x_lst[-1::-1])


if __name__ == "__main__":
    print(reverse_str("here is an example"))
