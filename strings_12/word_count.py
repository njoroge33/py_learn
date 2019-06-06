# Write a program to read English text and print a count of word lengths, i 
# e 
# the total number of words of length 1 which occurred, the number of length 2, and so on 
# for more info on this quiz, go to this url: http://www.programmr.com/word-count-4


def len_word(x_str):
    longest_word = ""
    for word in x_str.split():
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


if __name__ =="__main__":
    print(len_word("john gichuhi"))
