def is_valid(s):
	opening_brackes = "({["
	stack = []

	for i in s:
		if i in opening_brackes:
			stack.append(i)
		else:
			if not stack:
				return False

			if i == ")" and stack[-1] != "(" or \
			   i == "}" and stack[-1] != "{" or \
			   i == "]" and stack[-1] != "[":
				return False

			stack.pop()

	return len(stack) == 0

print(is_valid("]["))

