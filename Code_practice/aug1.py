import sys
import math

def solve():
	l1=[]
	l1=list(map(int,input().split()))
#	print(l1)
	h=l1[0]
	p=l1[1]
	if(p>=h):
		print("1")
	else:
		half=h/2
		if(p<=half):
			print("0")
		else:
			while(h>0 and p>0):
				h=h-p
				p=p/2

#			print(str(h)+" "+str(p))
			if(h<=0):
				print("1")
			else:
				print("0")
		

try:
	for tc in range(int(input())):
		solve()
except:
	pass
