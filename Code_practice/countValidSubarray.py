# number of valid subarrays
# Input : [1,4,2,5,3]
# Output : 11

# Explanation : There are 11 valid contiguous sub arrays whose leftmost element is not larger than than other element

def countValidSubarray(li):
	st = []
	res = 0
	for el in li:
		while not len(st) == 0 and el < st[-1]:
			st.pop()
		st.append(el)
		res += len(st)
	return res


li = [int(x) for x in input().split()]
print(countValidSubarray(li))



