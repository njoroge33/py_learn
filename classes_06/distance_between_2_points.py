# Create a class Point which prints the distance between two points p1(x1,y1) and p2(x2,y2)?
# for more info on this quiz, go to this url: http://www.programmr.com/distance-between-2-points-0
# formula = sqrt((x1 - x2)**2 + (y1 - y2)**2)


import math


class Point:
	def __init__(self, x_1, y_1, x_2, y_2):
		self.x_1 = x_1
		self.y_1 = y_1
		self.x_2 = x_2
		self.y_2 = y_2
		self.x = (self.x_1 - self.x_2)**2
		self.y = (self.y_1 - self.y_2)**2

	def diff(self):
		total = self.x + self.y
		return math.sqrt(total)


coordinates = Point(9, 7, 3, 2)

print(coordinates.diff())
