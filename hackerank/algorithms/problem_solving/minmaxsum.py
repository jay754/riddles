arr = [1,2,3,4,5]
results = []

def removeElement(element, array):
	s = 0
	for i in array:
		if i != element:
			s += i

	return s

for i in range(len(arr)):
	arr_sum = removeElement(arr[i], arr)
	results.append(arr_sum)

print(min(results), max(results))