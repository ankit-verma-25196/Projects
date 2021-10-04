# https://www.codechef.com/INPREP01/problems/FLOW016
# GCD and LCM

def solve():
	try:
		ab = list(map(int,input().split()))
	except:	
		pass

	a = ab[0]
	b = ab[1]
	
	c = min(a,b)
#	print(c)

	divisor = 0
	dividend = 0
	if c == a:
		divisor = a
		dividend = b
	else:
		divisor = b
		dividend = a

	while True:
		rem = dividend % divisor
		if rem != 0:
			dividend = divisor
			divisor = rem
		else:
			break

	print(divisor)
		

		
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass

