# o(n^2)
# def twoSum(array, target):
# 	for i in range(len(array)-1):
# 		for j in range(i+1, len(array)):
# 			if array[i] + array[j] == target:
# 				return (i, j)

# print(twoSum([3,2,4], 6))

def twoSum(array, target):
	a = {}

	for i in range(len(array)):
		memo = target - array[i]

		if memo not in a:
			a[memo] = i
		elif memo in a:
			return a[memo], i

print(twoSum([3,2,4], 6))