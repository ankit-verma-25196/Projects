import sys
import math

def solve():
	try:
		xyz=list(map(int,input().split()))
	except:
		pass

	xyz.sort()

	x=xyz[0]
	y=xyz[1]
	z=xyz[2]

#	print(str(x)+" "+str(y)+" "+str(z))

	if z == x+y:
		print("YES")
	else:
		print("NO")

	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
