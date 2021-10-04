import sys
import math

def solve():

	try:
		nkd=list(map(int,input().split()))
		p=list(map(int,input().split()))
	except:
		pass
	n=nkd[0] # number of problem setters
	k=nkd[1] # div-3 contest should have exactly k problems
	d=nkd[2] # contest will be for next d days, not more than 1 div-3 contest in a day# find max number of div-3 contests in d days
#	print(p)
	s=0
	for i in range(len(p)):
		s=s+p[i]

#	print("No. of problems = "+str(s))

	total=int(s/k)
#	print("Total = "+str(total))
		
	if total > d:
		print(d)
	else:
		print(total)

try:
	for tc in range(int(input())):
		solve()
except:
	pass
