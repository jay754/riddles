def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_array(arr):
    current_lcm = arr[0]
    for num in arr[1:]:
        current_lcm = lcm(current_lcm, num)
    return current_lcm

def gcd_of_array(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
    return current_gcd

def getTotalX(a, b):
    # Calculate the LCM of array `a`
    lcm_a = lcm_of_array(a)
    
    # Calculate the GCD of array `b`
    gcd_b = gcd_of_array(b)
    
    # Find the numbers that are multiples of `lcm_a` and divisors of `gcd_b`
    count = 0
    for x in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % x == 0:
            count += 1
    
    return count

# Example usage:
a = [2, 6]
b = [24, 36]
result = getTotalX(a, b)
print(result)

# def getTotalX(a, b):
#     count = 0

#     for i in range(1, 101):
#         is_valid = True
        
#         # Check if i is a multiple of all elements in array a
#         for element in a:
#             if i % element != 0:
#                 is_valid = False
#                 break
#             else:
#                 is_valid = True
        
#         # Check if i is a factor of all elements in array b
#         if is_valid:
#             for element in b:
#                 if element % i != 0:
#                     is_valid = False
#                     break
#                 else:
#                     is_valid = True
        
#         # If i satisfies both conditions, increment the count
#         if is_valid:
#             count += 1

#     return count

# # Example usage:
# a = [2, 6]
# b = [24, 36]
# print(getTotalX(a, b))  # Output: 2