# Min steps to make num -> 0 by subtracting Digits of num from num using DP
# 27 (-7) > 20 (-2) > 18 (-8) > 10 (-1) > 9 (-9) > 0

def getDigits(n):
	digits = []
	while n>0:
		if n%10 != 0:
			digits.append(n%10)
		n/=10
	print(digits)

	return digits

def solve():
	try:
		n = int(input())
	except:
		pass


	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
