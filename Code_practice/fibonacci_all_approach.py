# practice 

# calculate nth fibonacci using Pure Recursion
# T.C - O(2^n)
def fibPureRecursion(n):
	# base case
	if n <2:
		return n
	return fibPureRecursion(n-1)+fibPureRecursion(n-2)

# Nth Fibonacci using Top-Down DP Technique and using 'list' as 1 parameter for 1-D DP
# basically recursion will be used
# but since we are using DP, we will be storing unique sub-problems solutions in a data structure for purpose of time optimization
# It takes double passes - 1st to go to smallest subproblem and 2nd to calculate final solution
# T.C - O(2^n)
def fibDPTopDown(n,dp):
	if n <2:
		dp[n] = n
	if dp[n] != -1:
		return dp[n]

	dp[n] = fibDPTopDown(n-1,dp) + fibDPTopDown(n-2,dp)

	return dp[n]

# Nth Fibonacci using Bottom-Up DP Technique and using 'list' as 1 parameter for 1-D DP
# Here Recursion is not used
# will be storing unique sub-problems solutions in a 1-D data structure - lists
# It takes single pass - forward pass only becoz recursion is not used
def fibDPBottomUp(n,dp2):
	dp2[0] = 0
	dp2[1] = 1
		
	for i in range(2,n+1):
		dp2[i] = dp2[i-1] + dp2[i-2]

	return dp2[n]

# Nth Fibonacci using Bottom-Up DP Technique and using 2 variables only as 1 parameter for 1-D DP
# We are not required list/array since we don't need element till (i-3)th element for any ith element
# Here Recursion is not used
# will be storing unique sub-problems solutions in a 1-D data structure - variable
# It takes single pass - forward pass only becoz recursion is not used
def fibDPBottomUp_variable(n):
	a = 0
	b = 1
	c = 0
	for i in range(2,n+1):
		c = a+b
		a=b
		b=c

	if n==0:
		return a
	elif n==1:
		return b
	else:
		return c

try:
	n = int(input())
	print(fibPureRecursion(n))

	dp = [-1]*(n+1)
#	print(dp)
	print(fibDPTopDown(n,dp))

	dp2 = [0]*(n+1)
#	print(dp2)
	print(fibDPBottomUp(n,dp2))

	print(fibDPBottomUp_variable(n))

except:
	pass
