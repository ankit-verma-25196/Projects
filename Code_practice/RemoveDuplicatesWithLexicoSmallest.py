# remove duplicates lexicographically smallest
def remove_duplicates(s):
	stack = []
	visited = {}
	last_occ = {}

	for i in range(len(s)):
		last_occ[s[i]] = i
	
	for i in range(len(s)):
		ch = s[i]
		if visited.get(ch) == None:
			while not len(stack) == 0 and ch < stack[-1] and last_occ.get(stack[-1]) > i:
				visited.pop(stack[-1])
				stack.pop()

			visited[ch] = True
			stack.append(ch)

	result = ""

	for el in stack:
		result += el
	
	return result


	
s = input()
print(remove_duplicates(s))


