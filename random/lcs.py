def longestCommonSubsequence(text1, text2, m, n):
    if m == 0 or n == 0:
        return 0
    elif text1[m - 1] == text2[n - 1]:
        return 1 + longestCommonSubsequence(text1, text2, m - 1, n - 1)
    else:
        return max(
            longestCommonSubsequence(text1, text2, m - 1, n),
            longestCommonSubsequence(text1, text2, m, n - 1)
        )

'''

def allCommonSubsequences(text1, text2, m, n, current_subseq="", subsequences=None):
    if subsequences is None:
        subsequences = set()  # Initialize subsequences as a set to avoid duplicates

    if m == 0 or n == 0:
        if current_subseq:  # Only add non-empty subsequences
            subsequences.add(current_subseq)
        return subsequences

    if text1[m - 1] == text2[n - 1]:
        # Include the current character in the subsequence
        allCommonSubsequences(text1, text2, m - 1, n - 1, text1[m - 1] + current_subseq, subsequences)
    
    # Exclude the current character from either string
    allCommonSubsequences(text1, text2, m - 1, n, current_subseq, subsequences)
    allCommonSubsequences(text1, text2, m, n - 1, current_subseq, subsequences)

    return subsequences

# Test the function
s1 = "abcde"
s2 = "ace"
all_subsequences = allCommonSubsequences(s1, s2, len(s1), len(s2))
print(list(all_subsequences))

'''

s1 = "abcde"
s2 = "ace"

n = len(s1)
m = len(s2)

print(longestCommonSubsequence(s1, s2, n, m))

"""

                      lcs("ABCD", "AEBD")
                   /                         \
      lcs("ABC", "AEB")            lcs("ABCD", "AEB")
         /            \                     /               \
lcs("AB", "AE")     lcs("ABC", "AE")   lcs("ABC", "AEB") lcs("ABCD", "AE")


"""


# def longestCommonSubsequence(text1, text2, m, n):
# 	if m == 0 or n == 0:
# 		return 0
# 	elif text1[m - 1] == text2[n - 1]:
# 		return 1 + longestCommonSubsequence(text1, text2, m-1, n-1)

# s1 = "abcde"
# s2 = "ace"

# n = len(s1)
# m = len(s2)

# print(longestCommonSubsequence(s1, s2, n, m))