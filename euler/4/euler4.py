def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    largest = 0

    for i in range(1000):
        for j in range(1000):
            product = i * j
            
            if is_palindrome(product) and product > largest:
                largest = product
    
    return largest

print(largest_palindrome_product())