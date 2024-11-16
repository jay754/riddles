def isSubsequence(s, t):
    def recurse(i, j):
        # Base case 1: If we've reached the end of `s`, it's a subsequence
        if i == len(s):
            return True
        # Base case 2: If we've reached the end of `t` without fully matching `s`
        if j == len(t):
            return False
        # (Further logic would go here for recursion)
    
        if s[i] == t[j]:
            return recurse(i+1, j+1)
        elif s[i] != t[j]:
            return recurse(i, j+1)


    return recurse(0, 0)

print(isSubsequence("abc", "ahbgdc"))