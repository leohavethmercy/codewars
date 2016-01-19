# Sum Arrays

# Write a method sum (sum_array in python) that takes an array of numbers
# and returns the sum of the numbers. These may be integers or decimals for 
# Ruby and any instance of Num for Haskell. The numbers can also be negative.
# If the array does not contain any numbers then you should return 0.

Solution

def sum_array(a):
	return sum(a)


Tests

# test.describe("Testing sum_array")

# test.assert_equals(sum_array([]), 0)
# test.assert_equals(sum_array([1, 2, 3]), 6)
# test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
# test.assert_equals(sum_array([4, 5, 6]), 15)
# test.assert_equals(sum_array(range(101)), 5050)