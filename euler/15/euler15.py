'''

http://projecteuler.net/problem=15

i like this question

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many in a 20 by 20 grid?

http://mathworld.wolfram.com/BinomialCoefficient.html -> gives a pretty good explanation of why its a Binomial Coefficient	

I am not gonna lie there is no way in hell i would've got this question if I hadn't randomly googled pascal's triangle

'''

from math import factorial

def main():
	result = factorial(40) / (factorial(20)*factorial(40-20))
	print result

main()