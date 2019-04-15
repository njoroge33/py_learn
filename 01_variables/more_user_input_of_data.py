# The user is asked for several pieces of information. Display it on the screen as a summary. 
# First name: Helena
# Last name: Bonham-Carter
# Grade (9-12): 12
# student ID: 453916
# Login: bonham_453916
# GPA (0.0-4.0): 3.73
# Information-
# Login:bonham_453916
# ID:453916
# Name:Bonham-Carter; Helena
# GPA:3.73
# Grade:12
# for more info on this quiz, go to this url: http://www.programmr.com/more-user-input-data-3


def profile():
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    student_id = int(input("Enter your student ID:"))
    login = input("Enter your password:")
    gpa = float(input("Enter your GPA(0.0-4.0):"))
    grade = int(input("Enter your grade(9-12):"))
    print(" ")

    print(f"Name: {last_name},{first_name}")
    print(f"ID: {student_id}")
    print(f"Login: {login}")
    print(f"GPA: {gpa}")
    print(f"Grade: {grade}")
    return


print(profile())
