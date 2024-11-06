def is_happy(n):
    # Set to track encountered numbers and detect cycles
    numbers = set()

    while True:
        # Convert the integer to a string to access its digits
        num_str = str(n)

        # Sum the squares of each digit
        total = 0
        for char in num_str:
            digit = int(char)  # Convert the character back to an integer
            total += digit ** 2  # Square the digit and add to the total

        # If the sum is 1, the number is happy
        if total == 1:
            return True

        # If we've seen this sum before, it means we're in a cycle
        if total in numbers:
            return False

        # Add the current total to the set of seen numbers
        numbers.add(total)

        # Set n to the new total for the next iteration
        n = total

# Example usage
print(is_happy(19))  # Output: True
print(is_happy(2))   # Output: False