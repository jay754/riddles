def climbStairs(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n > 2:
		return climbStairs(n-1) + climbStairs(n-2)

print(climbStairs((5)))