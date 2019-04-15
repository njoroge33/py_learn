# Ask the user for their name 
# Then display their name to prove that you can recall it 
# Ask them for their age 
# Then display what their age would be five years from now 
# Then display what their age would be five years ago 
# for more info on this quiz, go to this url: http://www.programmr.com/age-five-years-3

name = input("Hello, What is your name: ")
age = int(input(f"{name}, How old are you: "))


def age_plus_five():
    total = age + 5
    return total


print(f"{name}, you will be {age_plus_five()} years old in five years from now")


def age_minus_five():
    total = age - 5
    return total


print(f"{name}, you were be {age_minus_five()} years old  five years ago")
