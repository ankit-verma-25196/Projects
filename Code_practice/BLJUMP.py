# Dynamic Programmming - https://www.codechef.com/UADPIP01/problems/BLJUMP
# jump over buildings

import sys

def solve():
	try:
		nk = list(map(int,input().split()))
		h = list(map(int,input().split()))
	except:
		pass

	n = nk[0]
	k = nk[1]
	
	max_ = float("inf")
#	print(max_)
	dp = [max_]*(n)

	dp[0] = 0
	for i in range(1,n):
		for j in range(1,k+1):
#			print("j="+str(j))
			if i-j < 0:
				break
			dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))

	print(dp[n-1])

try:
	for tc in range(int(input())):
		solve()
except:
	pass


