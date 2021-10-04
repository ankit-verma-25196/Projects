import sys
import math

def solve():
	l1=list(map(int,input().split()))
	k=l1[1]
	l2=list(map(int,input().split()))
#	print(l1)
#	print(l2)
	dic1={}
	for i in range(len(l2)):
		if(l2[i] < k):		
			if(k%l2[i]==0):
				div=k/l2[i]
				dic1[l2[i]]=div

#	print(dic1)
	if(len(dic1)==0):
		print("-1")
	else:
		minDiv=min(dic1.values())
#		print(minDiv)
		ans=0
		for num,div in dic1.items():
			if(div == minDiv):
				ans=num	
				break;
		print(ans)
	'''
	if (len(dic1)==0):
		print("-1")
	else:
		l3.sort()
		print(l3)
		print(l3[0])
	'''
				
			
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
