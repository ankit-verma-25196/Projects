# Min steps to make num -> 0 by subtracting Digits of num from num using DP
# 27 (-7) > 20 (-2) > 18 (-8) > 10 (-1) > 9 (-9) > 0

def getDigits(n):
	digits = []
	while n>0:
		if n%10 != 0:
			digits.append(n%10)
		n//=10
	print("IN Digits="+str(digits))

	return digits

def solve():
	try:
		n = int(input())
	except:
		pass

	if n <=9:
		print("1")
		return 0
	dp = [float('inf')]*(n+1)

	# for digits 1-9 , there is 1 way to make it to 0
	for i in range(1,10):
		dp[i] = 1
	
	for i in range(10,n+1):		
		# get the digits from number i
		digits = getDigits(i)
		print("OUT Digits="+str(digits))
		for j in range(len(digits)):
			dp[i] = min(dp[i],1+dp[i-digits[j]])

	print(dp[n])
	


	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
