# Filter the number

# Oh no! The number has been mixed up with the text. Your goal is to retreive the number from the text, can you return the number back to it's original state?

# Task

# Your task is to return a number from a string.

# Details

# You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string in the order they occur.


Solution

def filter_string(string):
	return int(string.translate(None, 'abcdedfghijklmnopqrstuvwxyz '))
   


Tests

Test.assert_equals(filter_string("123"), 123, 'Just return the numbers')
Test.assert_equals(filter_string("aa1bb2cc3dd"), 123, 'Just return the numbers')
Test.assert_equals(filter_string("aa 112 3dd"), 1123, 'Just return the numbers')
Test.assert_equals(filter_string("11bb2c23c3"), 112233, 'Just return the numbers')