def missing_number(nums):
    n = len(nums)
    
    # Calculate the expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the numbers in the array
    actual_sum = sum(nums)
    
    # The missing number is the difference between the expected sum and actual sum
    return expected_sum - actual_sum

# Example usage
print(missing_number([3, 0, 1]))  # Output: 2
print(missing_number([0, 1]))     # Output: 2