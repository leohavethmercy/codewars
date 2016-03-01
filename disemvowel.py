# # Problem:

# # Trolls are attacking your comment section!

# # A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# # Your task is to write a function that takes a string and return a new string with all vowels removed.

# # For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Solution(s):

# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")


# Test(s):

# test.assert_equals(disemvowel("This website is for losers LOL!"),
#                               "Ths wbst s fr lsrs LL!")


# def fizzbuzz(num):
# 	for i in xrange(num):
# 		if i%3==0 and i%5==0: print "fizzbuzz"
# 		elif i%3 == 0 : print 'fizz'
# 		elif i%5 == 0: print 'buzz'
# 		else: print i
		
# print fizzbuzz(101)

return [i for i in range(101) if i%3=0 and i%5==0 print "fizzbuzz" elif i%3 		== 0 print "fizz" else print i]

