def diagonal_difference(arr):
	straight_diagonals = []
	backwards_diagonals = []

	j = len(arr)

	for i in range(len(arr)):
		straight_diagonals.append(arr[i][i])
		backwards_diagonals.append(arr[i][j-1])
		j -= 1

	straight_sum = sum(straight_diagonals)
	backwards_sum = sum(backwards_diagonals)
	
	overall_sum = abs(straight_sum - backwards_sum)

	return overall_sum

print(diagnoal_difference(test))