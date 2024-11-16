"""

https://leetcode.com/problems/word-break/

"""

def word_break(s, wordDict, n):
    if n == 0:  # Base case for success
        return True
    if n < 0:  # Base case for failure
        return False

    