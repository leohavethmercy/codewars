# You have to create a function named reverseIt.
# Write your function so that in the case a string or a number is passed in as the data , you will return the data in reverse order. If the data is any other type, return it as it is.
# Examples of inputs and subsequent outputs:

def reverse_it(data):
	if type(data) == str: return data[::-1]
	elif type(data) == int: return int(str(data)[::-1])
	elif type(data) == float: return float(str(data)[::-1])
	else: return data

print reverse_it("Hello")
print reverse_it(123456)
print reverse_it(123.456)
print reverse_it([1,2,3,4,5,6])

# Clever solution I came across:

def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data

