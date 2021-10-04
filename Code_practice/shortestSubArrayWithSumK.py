import collections

def shortestsubarray(li, k):
	ans = float('inf') #infinite value for ans variable
	curr = 0
	d = collections.deque()
	pre = [0]*(len(li)+1)
	for i in range(len(li)):
		pre[i+1] = pre[i] + li[i] # storing with 1-based indexing

	for i in range(len(li)+1):
		while d and pre[i] - pre[d[0]]	>= k:
			ans = min(ans, i - d.popleft())

		while d and pre[i] <= pre[d[-1]]:
			d.pop()

		d.append(i)

	return ans if ans <= len(li) else -1

li = [int(x) for x in input().split()]
k = int(input())

print(shortestsubarray(li, k))
