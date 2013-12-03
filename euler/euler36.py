"""

http://projecteuler.net/problem=36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns all but the first character of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

def check_base():
	numbers = []

	for i in range(1000000):
		if is_palindrome(str(i)) and is_palindrome(str(bin(i)[2:])):
			numbers.append(i)

	return sum(numbers)

print check_base()