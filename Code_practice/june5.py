import sys
import math

def solve():
	try:
		n=int(input())
	except:
		pass
	if(n==1):
		print(1)
	elif(n%2!=0):
		i=1
		sq=n*n
		count=0
		while(i<=sq):
			print(str(i),end=" ")
			i+=1
			count+=1
			if(count==n):
				print()
				count=0
			
	elif(n%2==0):
		i=1
		sq=n*n
		count=0
		check=0
		j=0
		k=0
		while(i<=sq):
			if(k%2==0):
				print(str(i),end=" ")
				i+=1
				count+=1
			else:
				print(str(j),end=" ")
				i+=1
				j-=1
				count+=1
			if(count==n):
				print()
				count=0
				check+=1
				j=i+n-1
				k+=1
				
try:
	for tc in range(int(input())):
		solve()
except:
	pass
