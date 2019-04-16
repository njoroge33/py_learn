# Write a python program to ask the user for his/her name, age, and salary (double). Follow the input/output format.
# Following conversation should be displayed as output on screen, where you will enter the values of name,
# age and salary.
# Hello. What is your name?:
# John
# Hi John! How old are you?
# 22
# So you're 22 eh? That's not old at all!
# How much do you make John?
# 500
# 500.0! I hope that's per hour and not per year! LOL!
# for more info on this quiz, go to this url: http://www.programmr.com/name-age-and-salary-4


def conversing_user():
    name = input("Hello. What is your name?:\n")
    age = input(f"Hi {name}! How old are you?\n")
    print(f"so you're {age} eh? That's not old at all!")
    salary = float(input(f"How much do you make {name}:\n"))
    print(f"{salary}! I hope that's per hour and not per year! LOL!")


print(conversing_user())
