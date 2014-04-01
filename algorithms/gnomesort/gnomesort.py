def gnomesort(arr):
	i, j = 1, 2
	while i < len(arr):
		if arr[i-1] <= arr[i]:
			i , j = j, j + 1
		else:
			arr[i-1], arr[i] = arr[i], arr[i-1]
			i -= 1
			if i == 0:
				i, j = j, j + 1

	return arr

print gnomesort([5,4,3])