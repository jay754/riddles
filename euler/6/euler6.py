n = 100

sum_of_squares = sum(i**2 for i in range(1, n+1))

square_of_sum = sum(range(1, n+1)) ** 2

# Difference
difference = square_of_sum - sum_of_squares

print(difference)
