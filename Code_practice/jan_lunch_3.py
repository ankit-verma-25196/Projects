import sys
import math

def solve():
	try:
		nk=list(map(int,input().split()))	
		l1=list(map(int,input().split()))
	except:
		pass
	n=nk[0]
	k=nk[1]

	half=n/2
#	print(half)
	cVal=math.ceil(half)
#	print(cVal)

	
	notSolve=0
	tooSlow=0
	moreOne=0
	for i in l1:
		if i == -1:
			notSolve=notSolve+1
		elif i > k:
			tooSlow=tooSlow+1
		elif i > 1:
			moreOne=moreOne+1

	solve=n-notSolve

	if solve<cVal:
		print("Rejected")
	elif tooSlow>0:
		print("Too Slow")
	elif moreOne == 0 and notSolve == 0:
		print("Bot")
	else:
		print("Accepted")
		
#	print(notSolve)
#	print(tooSlow)
			

try:
	for tc in range(int(input())):
		solve()
except:
	pass
