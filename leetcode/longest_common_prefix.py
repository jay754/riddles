# https://leetcode.com/problems/longest-common-prefix/

s = ["flower","flow","flight"]

# def longestCommonPrefix(strings):
# 	smallest_string = min(strings,key=len)
# 	common_prefix = ""

# 	for i, ch in enumerate(smallest_string):
# 		for string in strings:
# 			if string[i] == ch:
# 				common_prefix += ch

# 	return(common_prefix)


# print(longestCommonPrefix(s))

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
            	# print(other[i], ch)
                if other[i] != ch:
                    return shortest[:i]
        # return shortest 

print(longestCommonPrefix(s))