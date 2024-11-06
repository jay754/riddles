def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False