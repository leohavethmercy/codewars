#7kyu
Description:
A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)
13 + 53 + 33 = 153

Write a method is_narcissistic(i) which returns whether or not i is a Narcissistic Number.


def is_narcissistic(i):
	total = 0
	number = i
	n = len(str(i))
	for i in str(i):
		total += int(i) ** n
	if total == number:
		print ("Narcissistic")
		return True
	else:
		print ("Not Narcissistic")
		return False

is_narcissistic(153)

#Test Cases

test.assert_equals(True, is_narcissistic(153))
test.assert_equals(False, is_narcissistic(201))
test.assert_equals(False, is_narcissistic(259))
test.assert_equals(True, is_narcissistic(371))
test.assert_equals(True, is_narcissistic(407))
test.assert_equals(False, is_narcissistic(595))
test.assert_equals(False, is_narcissistic(825))
test.assert_equals(True, is_narcissistic(1634))
