# Write a Python program that accepts a string as input from the user 
# Print "True" if the given string contains a "bob" string 
# If it does not print "False" 
# The middle "o" character can be any character 
# for more info on this quiz, go to this url: http://www.programmr.com/bob-there-1


def bob_there(x_str):
    for i in range(len(x_str)):
        if x_str[i] == "b" and x_str[i+2] == "b":
            return True
    return False


if __name__ == "__main__":
    print(bob_there("robbin"))
