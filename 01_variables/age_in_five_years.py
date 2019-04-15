# Ask the user for their name 
# Then display their name to prove that you can recall it 
# Ask them for their age 
# Then display what their age would be five years from now 
# Then display what their age would be five years ago 
# for more info on this quiz, go to this url: http://www.programmr.com/age-five-years-3

name = input("Hello, What is your name: ")
age = int(input("%s, How old are you: " % name))


def age_plus_five():
    total = age + 5
    return total


print(age_plus_five())


def age_minus_five():
    total = age - 5
    return total


print(age_minus_five())
