# maximum in sub-array of size k

from collections import deque

def print_max_in_all_subarray(arr, k):
	n = len(arr)
	qu = deque() # we can store indexes
	for i in range(k):
		while qu and arr[i] >= arr[qu[-1]]:
			qu.pop()
		qu.append(i)

	for i in range(k,n):
		print(arr[qu[0]])

		# do we need to slide window or not
		# out of bounds element check
		while qu and qu[0] <= i-k:
			qu.popleft()

		while qu and arr[i] >= arr[qu[-1]]:
			qu.pop()
		qu.append(i)

	# handling last sub array
	print(arr[qu[0]])

	return 

li = [int(x) for x in input().split()]
k = int(input())
print_max_in_all_subarray(li, k)
