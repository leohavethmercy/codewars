Problem:

Solution(s):
def divisors(integer):
	for i in iter(integer):
	    if integer % 2 == 0 or integer %3 ==0:
        	return i
        else:
        	return str(integer) + " is prime"
        	
        	
print divisors(15)
print divisors(12)
print divisors (7)


Test(s):