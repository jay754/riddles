"""

n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800

Let R(n) equal the sum of the digits in the number n!

For example, R(10) is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the lowest value for n where R(n) is 8001.

far as I got

"""

import math

def R(n):
  	numbers = [int(i) for i in str((math.factorial(n)))]
  	return sum(numbers)