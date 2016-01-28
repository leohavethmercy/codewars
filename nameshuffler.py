"""
Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john
"""

Solution(s)

def name_shuffler(str):
	str = ' ' .join(str.split()[::-1])
	return str

print name_shuffler('john McClane')
    	
		       	
Test(s)

Test.assert_equals(name_shuffler('john McClane'),'McClane john')
Test.assert_equals(name_shuffler('Mary jeggins'),'jeggins Mary')
Test.assert_equals(name_shuffler('tom jerry'),'jerry tom')