Problem:

Your job is to find out how much candy each child has, and give them each additional candy until they too have as much as the child(ren) with the most candy. You also want to keep a total of how much candy youve handed out because reasons.

Your job is to give all the kids the same amount of candies as the kid with the most candies and then return the total number candies that have been given out. If there are no kids, or only one, return -1.

In the first case (look below) the most candies are given to second kid (i.e second place in list/array), 8. Because of that we will give the first kid 3 so he can have 8 and the third kid 2 and the fourth kid 4, so all kids will have 8 candies.So we end up handing out 3 + 2 + 4 = 9.

Solution(s):

def candies(kids):
	total = 0
	for i in kids:
		while i < max(kids):
			i += 1
			total += 1
		if i <= 1:
			return -1
	if len(kids) <= 1:
		total -= 1
	return total

print candies([5,8,6,4])
print candies([1,2,4,6])
print candies([1,2])
print candies([4,2])
print candies ([3])
print candies ([])


Tests:

Test.assert_equals(candies([5,8,6,4]),9)
Test.assert_equals(candies([1,2,4,6]),11)
Test.assert_equals(candies([1,2]),1)
Test.assert_equals(candies([4,2]),2)

