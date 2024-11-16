# path = []

# def numSquares(n, path):
#     if n == 0:
#         return path
#     else:
#         for i in range(1, n + 1):  # start at 1 to avoid squaring 0
#             i_squared = i ** 2  # use ** for exponentiation
#             path.append(i_squared)
#             if i_squared > n:
#                 break
#             print(i_squared)
#             numSquares(n - i_squared, path)

# numSquares(10, [])

# List to store all valid combinations
results = []

def numSquares(n, path):
    # Base case: if n is zero, we've found a valid combination
    if n == 0:
        results.append(path[:])  # Append a copy of path to results
        return
    
    # Try each square number less than or equal to n
    for i in range(1, int(n**0.5) + 1):  # Limit to sqrt(n) for efficiency
        i_squared = i ** 2
        if i_squared > n:  # Ensure we're only adding valid squares
            break
        
        # Choose the square and add it to the path
        path.append(i_squared)
        
        # Recurse with reduced n and the updated path
        numSquares(n - i_squared, path)
        
        # Backtrack: remove the last square to try other combinations
        path.pop()

# Initial call with n=10 and an empty path
numSquares(5, [])

# Output all valid combinations
print("All combinations of squares that sum to 5:", results)


"""
                9
           /     |     \
         8       5       0
        /       / \
       7       4   1
      /       /     \
     6       3       0
    /       /
   5       2
  /       /
 4       1
/       /
3       0
|
2
|
1
|
0

"""

"""
https://leetcode.com/problems/perfect-squares/description/

def numSquares(n):
    # Initialize minimum count with a large number
    min_count = [float('inf')]  # Use a list to allow updating inside the nested function

    def recursiveCount(remaining, count):
        # Base case: if remaining is 0, we've found a valid solution
        if remaining == 0:
            min_count[0] = min(min_count[0], count)  # Update the minimum count if this path is shorter
            return
        
        # Try all square numbers <= remaining
        for i in range(1, int(remaining ** 0.5) + 1):
            square = i * i
            if square <= remaining:
                recursiveCount(remaining - square, count + 1)
    
    # Start the recursive search
    recursiveCount(n, 0)
    return min_count[0]

# Example usage:
print(numSquares(5))  # Expected output: 2 (since 4 + 1 = 5)
print(numSquares(12)) # Expected output: 3 (since 4 + 4 + 4 = 12)
print(numSquares(13)) # Expected output: 2 (since 9 + 4 = 13)

"""