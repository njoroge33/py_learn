# Documentation/Doc-string of a function/class can be accessed by using the " functinon/class name.__doc__" method.
# Create a class called "myClass" having the Doc-String :''This is my own created class."
# for more info on this quiz, go to this url: https://www.datacamp.com/community/tutorials/docstrings-python

class Myclass:
	def __init__(self, arg):
		self.arg = arg
	def add(a: int, b: int) -> int:
		"""Sums two numbers

		Args:
	    	a(int): one of the numbers.
	    	b(int): one of the numbers.

		Returns:
	    	The sum of the two numbers
		"""


	pass


