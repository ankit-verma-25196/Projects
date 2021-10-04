import sys
import math

def solve():
	list1 = []
	list1 = list(map(str,input().split()))
	s=int(list1[0])
	n=int(list1[1])
#	print(s)
#	print(n)
	quo=s/n
	rem=s%n
#	print(quo)
#	print(rem)
	if(rem == 0):
		print(int(quo))
	else:
		count=0
		if(rem ==1):
			count=int(quo)+1
			print(count)
		elif(rem > 1):
			if(rem%2==0):
				count=int(quo)+1
			else:
				count=int(quo)+2
			print(count)


try:
	for tc in range(int(input())):
		solve()
except:
	pass
