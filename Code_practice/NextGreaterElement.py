# Given a list of integers, find next greater element for each of the elements in the list
# 10,7,4,2,9,10,11,3,2 --> i/p
# 11,9,9,9,10,11,-1,-1,-1 -->o/p
# T.C -> O(n)
# S.C -> O(n)

def nextGreater(li):
	n = len(li)	
	result = [-1]*n
	st = []
	for i in range(n):
		while not len(st) == 0 and li[st[-1]] < li[i]:
			popped = st[-1]
			st.pop()
			result[popped] = li[i]
		st.append(i)

	return result

def nextGreaterCircular(li):
	n = len(li)	
	result = [-1]*n
	st = []
	for i in range(2*n):
		while not len(st) == 0 and li[st[-1]] < li[i%n]:
			popped = st[-1]
			st.pop()
			result[popped] = li[i%n]
		st.append(i%n)

	return result


li = [int(x) for x in input().split()]
print(nextGreaterCircular(li))

