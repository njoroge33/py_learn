# Define a class Circle
# The circle takes a radius
# Compute the area of the circle
# for more info on this quiz, go to this url: http://www.programmr.com/circle-class-3


import math
pie = math.pi


class Circle:
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return  pie * (self.radius ** 2)

radius = Circle(7)

print(radius.area())
