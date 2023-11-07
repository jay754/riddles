arr = [5,5,5,5,5]
results = []

def removeElement(element, array):
    s = 0
    for i in array:
        if i != element:
            s += i

    return s

def miniMaxSum(arr):
	results = []

	for i in range(len(arr)):
		arr_sum = removeElement(arr[i], arr)
		results.append(arr_sum)

	print(min(results), max(results))

miniMaxSum(arr)