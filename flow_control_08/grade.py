# Write a function grader that when  given a dict marks scored by a student in different subjects
# prepares a report for each grade as A,B,C and FAIL and the average grade
# example: given
# marks = {'kisw': 34, 'eng': 50}
# return
# {'kisw': 'FAIL', 'eng': 'C', 'average': 'D'}
# A = 100 - 70, B = 60 - 70, C = 50 - 60, D = 40 - 50, FAIL = 0 - 39
# average is calculated from the number of subjects in the marks dict
# for more info on this quiz, go to this url: http://www.programmr.com/grade


class InvalidScore(ValueError):
	pass


def gen_report_x(marks):
	pass


def average(scores):
	return int(sum(scores) / len(scores))


def grade(score):
	if score >= 70:
		return "A"
	elif score >= 60:
		return "B"
	elif score >= 50:
		return "C"
	elif score >= 40:
		return "D"
	else:
		return "FAIL"


def gen_report(marks):
	report = {}
	for i in marks:
		if marks[i] > 100:
			raise InvalidScore(f'Score: {marks[i]} for subject: {i} exceeds maximum score of a 100.')
		report[i] = grade(marks[i])
	report["average"] = grade(average(marks.values()))
	return report


if __name__ == '__main__':
	try:
		print(gen_report({'Eng': 10, 'Kisw': 20, 'C.R.E': 40}))
	except Exception as err:
		print(err)
