'''

http://projecteuler.net/problem=8

Find the greatest product of five consecutive digits in the 1000-digit number.

THIS QUESTION SUCKS

i thought it was consecutive numbers not digits

'''

def main():
	number = open('euler8.txt', 'r')

	numbers = []

	for i in number:
		for j in i:
			if j != "\n":
				numbers.append(j)

	max_num = 0

	for i in range(len(numbers)-4):
		product = int(numbers[i]) * int(numbers[i+1]) * int(numbers[i+2]) * int(numbers[i+3]) * int(numbers[i+4])
		if product > max_num:
			max_num = product

	print max_num

main()