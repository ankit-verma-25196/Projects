import sys
import math

def solve():
	try:
		n = input()
	except:
		pass
	l1 = list(map(int,input().split()))
#	print("List="+str(l1))
	sum = 0
	countN = 0
	countP = 0
	for i in range(len(l1)):
		j = i+1
		if l1[i] < 0:
			countN += 1
		if l1[i]%j == 0:
			countP += 1
		sum += l1[i]
	
	if sum == 0:
		print("YES")
	elif sum < 1:
		print("NO")
	elif sum > 0:
		if countP == len(l1):
			print("YES")
		else:
			print("NO")
	

try:
	for tc in range(int(input())):
		solve()
except:
	pass
