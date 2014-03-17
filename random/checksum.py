"""

http://en.wikipedia.org/wiki/Fletcher%27s_checksum

Fletcher-16

"""

def checksum(data):

	sum1 = 0
	sum2 = 0

	for i in data:
		sum1 = (sum1 + ord(i)) % 255
		sum2 = sum1 + sum2 % 255

	return (sum2 << 8) | sum1