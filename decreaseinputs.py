# Problem:

# This kata is all about adding numbers.

# You will create a functin named add. This function will return the sum of all the arguments. Sounds easy, doesnt it??

# Well Here the Twist. The inputs will gradually decrease with their index as parameter to the function.

#   add(3,4,6) #returns (3/1)+(4/2)+(6/3)=7
# Remember the function will return 0 if no arguments is passed and the function must round the values if sum is a float.

# Solution(s):

def add(*args):
    num = 1
    adder = 0
    for i in args:
        i = i/float(num)
        adder += i
        num += 1
    return round(adder)

# Test(s):

Test.assert_equals(add(100,200,300),300)
Test.assert_equals(add(2),2)
Test.assert_equals(add(4,-3,-2),2)




