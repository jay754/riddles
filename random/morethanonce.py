'''

From an input file, print any character that occurs more than once, but only print it once.

Input: "Hello World"

Output: "l o"

'''

def main():
	
	'''
		I am a hundered percent sure there is an easier way to do this

		if anyone knows please let me know

		This is actually a terrible solution even tho it works
	'''

	results = open('input.txt', 'r')
	
	chars = ''

	histo = {}
	#temp = []
	for i in results:
		for char in i:
			if histo.has_key(char):
				histo[char] += 1
			else:
				histo[char] = 1

	for k, v in histo.iteritems():
		if v > 1:
			print k

main()