import sys
import math

def solve():
	l1=list(map(int,input().split()))
#	print(l1)
	cPow=l1[0]
	rPow=l1[1]
	if(cPow <=9 and rPow <=9):
		print("1 1")
	else:
		if(cPow >= rPow ):
			rScore=0
			rScore=int(rPow/9)
			rRem = rPow%9
#			print(rRem)
			if(rPow%9 != 0):
				rScore+=1
			print(str(1)+" "+str(rScore))
				
		else:
			cScore=0
			cScore=int(cPow/9)
			cRem = cPow%9
#			print(cRem)
			if(cPow%9 != 0):
				cScore+=1
			print(str(0)+" "+str(cScore))		
		'''
		if(cPow>9):
			cNum=9
			cInitialArr=[9]
			while(cNum < cPow):
				cDiff=cPow-cNum
				if(cDiff<=9):
					cInitialArr.append(cDiff)
					break;
				else:
					cInitialArr.append(int(9))
					cNum+=9
#			print(cInitialArr)
			cScore=len(cInitialArr)
		if(rPow>9):
			rNum=9
			rInitialArr=[9]
			while(rNum < rPow):
				rDiff=rPow-rNum
				if(rDiff<=9):
					rInitialArr.append(rDiff)
					break;
				else:
					rInitialArr.append(int(9))
					rNum+=9
#			print(rInitialArr)
			rScore=len(rInitialArr)
		if(rScore<=cScore):
			print(str(1)+" "+str(rScore))
		else:
			print(str(0)+" "+str(cScore))
		'''
					
try:
	for tc in range(int(input())):
		solve()
except:
	pass
