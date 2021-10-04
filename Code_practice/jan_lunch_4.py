import sys
import math

def solve():
	try:
		n=int(input())	
		l1=list(map(int,input().split()))
	except:
		pass

	odd = 0
	even = 0
	
	for i in l1:
		if i % 2 == 0:
			even = even +1
	
	odd = n-even

	if odd % 2 == 0: # number of odd numbers are odd , then final value even --->1 wins else -->2 wins
		print("1")
	else:
		print("2")

try:
	for tc in range(int(input())):
		solve()
except:
	pass
