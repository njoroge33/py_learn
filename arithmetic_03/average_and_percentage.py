# Marks obtained by a student in four different subjects are given calculate tha average marks(2 decimals)
# Maximum marks that can be obtained by student in each subject is 100
# example; given the following marks, 56, 78, 90 and 87
# you should return 77.5
# for more info on this quiz, go to this url: http://www.programmr.com/average-and-percentage


def average(a, b, c, d):
    if a > 100 or b > 100 or c > 100 or d > 100:
        return "Invalid mark"
    else:
        return round((a + b + c + d)/4, 2)


if __name__ == "__main__":
    print(average(56, 78, 90, 87))
