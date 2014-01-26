'''
http://projecteuler.net/problem=12

What is the value of the first triangle number to have over five hundred divisors?

'''

def factors(n):
	#http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def triangular_number(n):
	return n*(n+1)/2

def main():

	i = 1
	counter = 0

	while True:
		t_num = triangular_number(i)
		num_factors = factors(t_num)

		if len(num_factors) > 500:
			counter += t_num
			break

		i += 1

	print counter

main()