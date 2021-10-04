import sys
import math

def solve():
	try:
		n=int(input())
	except:
		pass
	l1 = []
	l1 = list(map(int,input().split()))
#	for i in range(len(l1)):
#		print(l1[i])
#	l2=sorted(l1)
	l1.sort()
#	print("list now : ",l1)

	
	j=0
	l3=set(l1)
	print(l3)
	flag = len(set(l3)) == len(l1)
#	print("flag="+str(flag))

	if(flag):
		print("YES")
		for j in range(len(l1)):
			print(l1[j],end=' ') 
		print()
	else:
		counter=0
		k=0
		while(k<(len(l1)-1)):
			if(l1[k]==l1[k+1]):
				k+=2
			else:
				counter=1
				break	
			
		if(counter==1):
			print("NO")	
		else:
			print("YESS")
			if(len(l3)%2==0):
				for l in range(len(l3)):
					print(l3[l],end=' ')
				l=len(l3)-1
				while(l>=0):
					print(l3[l],end=' ')
					l-=1
				print()
			else:
				for l in range(len(l3)-1):
					print(l3[l],end=' ')
				print(l3[len(l3)-1],end=' ')
				l=len(l3)-2
				while(l>=0):
					print(l3[l],end=' ')
					l-=1
				print()		



try:
	for tc in range(int(input())):
		solve()
except:
	pass
