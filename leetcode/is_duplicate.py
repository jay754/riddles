def contains_duplicate(nums):
    # Dictionary to track frequency of numbers
    num_count = {}

    for num in nums:

        if num in num_count:
            return True

        num_count[num] = 1

    return False

# Example usage
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
print(contains_duplicate([1, 2, 3, 4]))  # Output: False