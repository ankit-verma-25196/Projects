import sys
import math

def solve():
	try:
		n = int(input())
		w = list(map(int,input().split())) # weight of frogs
		l = list(map(int,input().split())) # jump length of frogs
	except:
		pass

#	print(w)
#	print(l)

	ans=0

	if n == 2:	
		if w[0]>w[1]:
			if l[0]==1:
				ans=2
			else:
				ans=1


	elif n > 2:
		for i in range(len(w)):
			if w[i]-1
		
	print(ans)


try:
	for tc in range(int(input())):
		solve()
except:
	pass


# 2 1 4 3




