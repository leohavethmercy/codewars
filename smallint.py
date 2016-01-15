# Find the smallest integer in the array


# Uses pythons built in function min
def findSmallestInt(arr):
	return min(arr)

# OR

# Iterating with a for loop over the list
def findSmallestInt(arr):
	currentn = arr[0]
	for n in arr:
		if n < currentn: currentn = n
	return currentn


# Tests
test.assert_equals(findSmallestInt([78,56,232,12,11,43]), 11)

test.assert_equals(findSmallestInt([78,56,-2,12,8,-33]), -33)

test.assert_equals(findSmallestInt([0, -1-sys.maxint,sys.maxint]), -1-sys.maxint)