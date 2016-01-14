# Simply, create a method for the class Dog which (when called) will return the string 'Woof!'

# Solution

class Dog(object):
	def __init__(self, name, breed, sex, age):
		self.name = name
		self.breed = breed
		self.sex = sex
		self.age = age

	def bark(self):
    	return 'Woof!'
        
# Tests

print 'Can you make newly created dogs bark?'
apollo = Dog('Apollo', 'Dobermann', 'male', '4')
zeus = Dog('Zeus', 'Dobermann', 'male', '4')

Test.assert_equals(apollo.bark(), 'Woof!')
Test.assert_equals(zeus.bark(), 'Woof!')