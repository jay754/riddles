def plus_one(digits):
    num_str = ''.join(map(str, digits))
    
    num = int(num_str) + 1
    
    return [int(digit) for digit in str(num)]

# Example Test Case
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]