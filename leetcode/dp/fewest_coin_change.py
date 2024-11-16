def coinChange(coins, amount):
	if amount == 0:
		return 0

	min_coins = float('inf')

	for i in range(len(coins)):
		if amount - coins[i] >= 0:
		    result = coinChange(coins, amount - coins[i])
		    if result != float('inf'):
		    	min_coins = min(min_coins, result + 1)


	return min_coins if min_coins != float('inf') else -1

coins = [1,2,5]

print(coinChange(coins, 11))

"""

 						   11
                /          |          \
              6            9            10
           /   |   \     /   |   \     /   |   \
         1     4     5  4     7    8  5     8    9

"""


# def coinCombinations(coins, amount):
#     result = []

#     def findCombinations(remaining, path):
#         # Base case: if remaining is 0, a valid combination is found
#         if remaining == 0:
#             result.append(path)
#             return
#         # If remaining becomes negative, this path is invalid
#         if remaining < 0:
#             return

#         # Try each coin and recurse with the updated amount and path
#         for coin in coins:
#             findCombinations(remaining - coin, path + [coin])

#     findCombinations(amount, [])
#     return result

# # Example usage:
# coins = [1, 2, 5]
# amount = 5
# print(coinCombinations(coins, amount))  # Output: All combinations to make up amount 5
