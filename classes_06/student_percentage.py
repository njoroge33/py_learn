# A class student has three data members: name, roll, marks of 5 subjects
#       and two member functions:
# member ():to input name, roll no and marks
# Display ():to display Percentage
# Declare the class student and define the member functions
# The program should ask user for name, roll no and marks in 5 subjects, and should display the percentage
# for more info on this quiz, go to this url: http://www.programmr.com/student-percentage-2


class Student:
    def __init__(self, name, roll_num, math, english, kisw, chem, hist):
        self.name = name
        self.roll_num = roll_num
        self.math = math
        self.english = english
        self.kisw = kisw
        self.chem = chem
        self.hist = hist

    @classmethod
    def member(cls):
        return cls(input('Name: '), input('Roll No: '), int(input('Math: ')),
                   int(input('english: ')), int(input('kisw: ')), int(input('chem: ')), int(input('hist: ')))

    def display_per(self):
        total = ((self.math + self.english + self.kisw + self.chem + self.hist) / 500) * 100
        return total



user = Student.member()

print(user.display_per())
