"""

i hate this question

https://leetcode.com/problems/decode-ways/

                         num_decodings("226")
                         /            |             \
              Decode '2' → 'B'   Decode '22' → 'V'   Invalid
                      |                   |
            num_decodings("26")          num_decodings("6")
            /            |               /
     Decode '2' → 'B'   Decode '26' → 'Z'
            |                   |
     num_decodings("6")       num_decodings("") → 1
          |
     Decode '6' → 'F'  
          |
     num_decodings("") → 1

"""

def num_decodings(s):
    # Recursive helper function
    def helper(index):
        # If we've reached the end of the string, return 1 as a valid decoding
        if index == len(s):
            return 1
        # If the current character is '0', it cannot be decoded
        if s[index] == '0':
            return 0
        
        # Initialize the number of ways to decode from the current index
        ways = helper(index + 1)
        
        # Check if the next two characters form a valid number between 10 and 26
        if index + 1 < len(s):
            two_digit = int(s[index:index + 2])
            if 10 <= two_digit <= 26:
                ways += helper(index + 2)
        
        return ways
    
    # Edge case: empty string
    if not s:
        return 0
    
    # Start recursion from the first character
    return helper(0)

# Example Usage:
s = "226"
print(num_decodings(s))  # Output: 3
