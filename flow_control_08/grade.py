# Write a function grader that when  given a dict marks scored by a student in different subjects
# prepares a report for each grade as A,B,C and FAIL and the average grade
# example: given
# marks = {'kisw': 34, 'eng': 50}
# return
# {'kisw': 'FAIL', 'eng': 'C', 'average': 'D'}
# A = 100 - 70, B = 60 - 70, C = 50 - 60, D = 40 - 50, FAIL = 0 - 39
# average is calculated from the number of subjects in the marks dict
# for more info on this quiz, go to this url: http://www.programmr.com/grade


class InvalidError(Exception):
    pass


def average(marks):
    a = int(sum(marks.values())/len(marks))
    return a


def grades(score):
    if score > 100:
        raise InvalidError("Invalid mark")
    elif score >= 70:
            return "A"
    elif score >= 60:
            return "B"
    elif score >= 50:
            return "C"
    elif score >= 40:
            return "D"
    elif score < 40:
            return "FAIL"


def gen_report(marks):
    marks["average"] = average(marks)
    for i in marks:
        marks[i] = grades(marks[i])
    return marks


print(gen_report({'aen302': 80, 'aen303': 70, 'alt302': 55, 'alt303': 70}))
