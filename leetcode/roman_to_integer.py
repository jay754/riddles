def romanToInt(s):

	nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

	output = 0

	for letter in range(len(s)-1):
		if nums[s[letter+1]] > nums[s[letter]]:
			output -= nums[s[letter]]
		else:
			output += nums[s[letter]]

		print (output)

	print(output + nums[s[-1]])

romanToInt("XVI")