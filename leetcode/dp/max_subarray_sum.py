"""

Kadane's algorithm

https://leetcode.com/problems/maximum-subarray/description/

"""

def max_subarray(nums):
    # Initialize variables
    max_current = max_global = nums[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Update the current maximum subarray sum
        max_current = max(nums[i], max_current + nums[i])

        # Update the global maximum subarray sum if needed
        if max_current > max_global:
            max_global = max_current

    return max_global

# Example Usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 