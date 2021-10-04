import math
import sys

def solve():
	try:
		n = int(input())
	except:
		pass

	i=2
	max=1
	while i<=10:
		if n%i == 0:
			max=i

		
		i=i+1

	print(max)

try:
	solve()
except:
	pass


