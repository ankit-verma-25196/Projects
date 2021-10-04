import math
import sys

def solve():
	try:
		n=int(input())
		l1=list(map(int,input().split()))
	except:
		pass

	even = 0
	odd = 0

	for i in l1:
		if i % 2 == 0:
			even=even+1
		else:
			odd=odd+1

	if even == 0 or odd == 0:
		print("0")
	else:
		if odd > even:
			print(even)
		else:
			print(odd)
			
	

try:
	for tc in range(int(input())):
		solve()
except:
	pass
