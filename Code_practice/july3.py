import math
import sys

def solve():
	try:
		k = int(input())
	except:
		pass

	for i in range(8):
		for j in range(8):
			ii=i-0
			jj=j-0
			counti=math.pow(ii,2)
			countj=math.pow(jj,2)
			countij=counti+countj
#			print(str(counti))
#			print(str(countj))
			if(i==0 and j==0):
				print("0",end="")
			elif(k>1):
				print(".",end="")
				k-=1
			elif(countij<=2):
				print("X",end="")
			else:
				print(".",end="")
		print()
try:
	for tc in range(int(input())):
		solve()
except:
	pass
