import sys
import math

def solve():
	
	try:
		l1= list(map(int,input().split()))	
		k = int(input())
	except:
		pass

	max1 = 0

	for i in range(len(l1)):
		if l1[i] > max1:
			max1 = l1[i]
	print(max1)
	


try:
	for tc in range(int(input())):
		solve()
except:
	pass
