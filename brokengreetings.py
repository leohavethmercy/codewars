# Broken Greetings
# Correct this code, so that the greet function returns the expected value.

Class Person:
	def __init__ (self, name):
	def greet(self, other_name):
		return "Hi {0}, my name is {1}".format(other_name, name)

# Solution

Class Person:
	def __init__ (self, name):

	def greet(self, other_name):
		return "Hi {0}, my name is {1}".format(other_name, self.name)