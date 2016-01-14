# Find the number of points someone has scored on varying tests of different lengths. The given parameters will be:

# 1) An array containing a series of 0s, 1s, and 2s, where the 0s are the correct answers, the 1s are the omitted answers, and the 2s are the incorrect answers.

# 2) The points awarded for correct answers

# 3) The points awarded or deducted for omitted answers (note that this will either be positive or negative)

# 4) The points deducted for incorrect answers (This value is to be subtracted)

# Solution

def score_test(tests, right, omit, wrong):
    score = (
    	right * tests.count(0) +
    	omit * tests.count(1) -
    	wrong * tests.count(2) 
    )
    return score

 
print score_test([0, 0, 0, 0, 2, 1, 0], 2, 0, 1)
print score_test([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2)

# Test

Test.assert_equals(score_test([0, 0, 0, 0, 2, 1, 0], 2, 0, 1), 9);
Test.assert_equals(score_test([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2), 3)