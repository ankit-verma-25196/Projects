# Billiard/Pool Table Problem

import sys
import math

def solve():
	try:
		nkxy=list(map(int,input().split()))
	except:
		pass
	n=nkxy[0]
	k=nkxy[1]
	x=nkxy[2]
	y=nkxy[3]

#	print(str(n)+","+str(k)+","+str(x)+","+str(y))

	if x==y:
		print(str(n)+" "+str(n))
	else:
		p1=None
		p2=None
		p3=None
		p4=None
		pt=k%4
		if x > y:
			if pt == 1:
				print(str(n)+" "+str(y+n-x))
			elif pt == 2:
				print(str(y+n-x)+" "+str(n))
			elif pt == 3:
				print("0 "+str(x-y))
			elif pt == 0:
				print(str(x-y)+" 0")

		elif y > x:
			if pt == 1:
				print(str(x+n-y)+" "+str(n))
			elif pt == 2:
				print(str(n)+" "+str(x+n-y))
			elif pt == 3:
				print(str(y-x)+" 0")
			elif pt == 0:
				print("0 "+str(y-x))
			
			

try:
	for tc in range(int(input())):
		solve()
except:
	pass
