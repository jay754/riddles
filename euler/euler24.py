'''

http://projecteuler.net/problem=24

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

from itertools import permutations as p

count = 0

for i in p("0123456789"):
	if count == 999999:
		print ''.join(i)
		break
	count += 1