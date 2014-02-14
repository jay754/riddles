'''

http://projecteuler.net/problem=56

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

'''

def digital_sum(s):
	#http://en.wikipedia.org/wiki/Digital_sum
	return sum(int(i) for i in str(s))

def main():
	num = 0
	for a in range(1,101):
		for b in range(1,101):
			temp = digital_sum(pow(a,b))
			if temp > num:
				num = temp

	print num

main()