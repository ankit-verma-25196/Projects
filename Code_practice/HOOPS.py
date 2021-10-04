# https://www.codechef.com/LTIME96C/problems/HOOPS

import math

def solve():
	try:
		n = int(input()) # n will be odd
	except:
		pass
	print(math.ceil(n/2))
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
