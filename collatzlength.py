# The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. If you repeat the process continously for n, n will eventually reach 1.

# For example, if n = 20, the resulting sequence will be:

# [20, 10, 5, 16, 8, 4, 2, 1]

# Write a program that will output the length of the Collatz Conjecture for any given n. In the example above, the output would be 8.

# For more reading see: http://en.wikipedia.org/wiki/Collatz_conjecture

Solution

def collatz(n):
    Mylist = []
    Mylist.append(n)
    while n != 1:
        if (n%2==0):
            n = (n//2)
            Mylist.append(n)
        else:
            n = (n*3+1)
            Mylist.append(n)
    return len(Mylist)

Tests

test.assert_equals(collatz(20), 8)
test.assert_equals(collatz(15), 18)

#This was fun, haven't used a while loop in a while.