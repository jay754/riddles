"""
https://leetcode.com/problems/combination-sum-iv/description/

"""

def combination_sum_iv(nums, target):
    # Base case: if the target is zero, there's one valid way to form the sum
    if target == 0:
        return 1
    # If the target is negative, no valid combination exists
    if target < 0:
        return 0

    # Initialize count of combinations for the current target
    count = 0
    # Iterate through each number in nums
    for num in nums:
        # Recursively call the function with the reduced target
        count += combination_sum_iv(nums, target - num)

    return count

# Example Usage:
nums = [1, 2, 3]
target = 4
print(combination_sum_iv(nums, target))  # Output: 7


"""
						combinations_sum(4)
                    /         |         \
              (choose 1)  (choose 2)  (choose 3)
                  |            |             |
          combinations_sum(3)  combinations_sum(2)  combinations_sum(1)
             /      |      \         /       |       \         |
        (choose 1) (choose 2) (choose 3) (choose 1) (choose 2) (choose 3)
              |          |         |         |         |         |
      combinations_sum(2) combinations_sum(1) combinations_sum(0) (invalid) 
          /     |     \           |            | 
 (choose 1) (choose 2) (choose 3) (choose 1) (choose 0)
     |           |          |           |
combinations_sum(1)  combinations_sum(0) (invalid)
      /    |    \       |
(combine 1)(combine 2)(combine 0)



"""