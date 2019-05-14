# Write a program that takes student's grade point average and SAT exam score,
# and uses these values to decide whether the student is admitted to the university.
# A GPA below 1.8 will cause the student to be rejected; and a SAT score below 900 will also cause a rejection.
# Otherwise the student is accepted.
# return True if admitted or False if not
# for more info on this quiz, go to this url: http://www.programmr.com/devry-admission-program-0


def is_admitted(gpa, sat):
    try:
        if gpa < 1.8 or sat < 900:
            return False
        return True
    except TypeError:
        return "Wrong data type!: gpa and sat expected as integers or float"


if __name__ == "__main__":
    print(is_admitted(2, "1.8"))
