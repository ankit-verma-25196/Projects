import sys
import math

def solve():
	try:
		n = int(input())
	except:
		pass
	l1=list(map(int,input().split()))
#	print(l1)
	# Converting the list into set to get distinct elements
	l1_set = set(l1)
	len_set = len(l1_set)
	if 0 in l1_set:
		print(len_set-1)
	else:
		print(len_set)
	
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
