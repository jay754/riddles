def singleNumber(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in freq:
        if freq[num] == 1:
            return num

# Example usage
print(singleNumber([2, 2, 1]))  # Output: 1
print(singleNumber([4, 1, 2, 1, 2]))  # Output: 4