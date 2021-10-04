# https://www.codechef.com/UADPIP01/problems/FIBONUM

def fibTopDown(n,dp):
	if n == 0 or n == 1:
		return n

	# return nth fibonacci if already calculated
	if dp[n] != -1:
		return dp[n]

	# calculate nth state fibonacci first time
	mod = 1000000007
	dp[n] = fibTopDown(n-1,dp)%mod+fibTopDown(n-2,dp)%mod
	return dp[n]

	
def solve():
	try:
		 n = int(input())
	except:
		pass

	dp = [-1]*(n+1)
	# solving using top down DP
	print(fibTopDown(n,dp))
	


try:
	for tc in range(int(input())):
		solve()
except:
	pass
