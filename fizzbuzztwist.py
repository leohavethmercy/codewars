# Write a function that takes an integer and returns an Array [A, B, C] where A is the number of multiples of 3 (but not 5) less than the given integer, B is the number of multiples of 5 (but not 3) less than the given integer and C is the number of multiples of 3 and 5 less than the given integer.

# For example, solution(20) should return [5, 2, 1]

Solutions

def solution(number):

  A = len([x for x in range(1,number) if x%3 == 0 and x%5 != 0])
  B = len([x for x in range(1,number) if x%5 == 0 and x%3 != 0])
  C = len([x for x in range(1,number) if x%3 == 0 and x%5 == 0])
  
  return [A,B,C]

Tests

test.assert_equals((solution(20)), [5,2,1])
test.assert_equals((solution(2)), [0,0,0])
test.assert_equals((solution(30)), [8,4,1])
test.assert_equals((solution(300)), [80,40,19])
