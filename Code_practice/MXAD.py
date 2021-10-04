# https://www.codechef.com/UADPIP01/problems/MXAD

def solveRecursion(n,l1):
	if n == 0:
		return l1[0]
	if n == 1:
		return max(l1[0],l1[1])
	return max(solveRecursion(n-1,l1), l1[n]+solveRecursion(n-2,l1))

#global dp array
dp = [-1]*(100005)

def solveDPTopDown(n,l1):
	
	if n == 0:
		return l1[0]
	if n == 1:
		return max(l1[0],l1[1])
	if dp[n] != -1:
		return dp[n]
	dp[n] = max(solveRecursion(n-1,l1), l1[n]+solveRecursion(n-2,l1))
	return dp[n]

def solveDPBottomUp(n,l1):	
	dp = [0]*(n+1) # 1 based indexing
	
	dp[0] = l1[0]
	dp[1] = max(l1[0],l1[1])

	for i in range(2,n+1):
		dp[i] = max(dp[i-1],l1[i]+dp[i-2])
	return dp[n]

def solve():
	try:
		n = int(input())
		l1 = [0]*(n+1)
		#print(len(l1))
		s = list(map(int,input().split()))
		#print(s)
		for i in range(n):
			l1.insert(i+1,s[i])
		#print(l1)

	except:
		pass
	print(solveRecursion(n,l1))

	#initialise dp list with size just larger than max list size AND with value default to -1
	
	print("using top down DP")
	print(solveDPTopDown(n,l1))

	print("using bottom up DP")
	print(solveDPBottomUp(n,l1))
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
