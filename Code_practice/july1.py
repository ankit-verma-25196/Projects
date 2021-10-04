import sys
import math

def solve():
	try:
		n = int(input())
	except:
		pass
	l1 = []
	l1 = list(map(int,input().split()))
#	print(l1)
	sum=0
	for i in range(len(l1)-1):
		if(l1[i]>l1[i+1]):
			diff=l1[i]-l1[i+1]-1
		elif(l1[i]<l1[i+1]):
			diff=l1[i+1]-l1[i]-1
		sum+=diff
	print(sum)
			
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass

