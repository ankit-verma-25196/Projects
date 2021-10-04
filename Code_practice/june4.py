import sys
import math

def solve():
	try:
		n=int(input())
	except:
		pass
	i=1
	count=0
	while(i<=n):
		if(i%2==0):
			count+=1
		i+=1
	print(count)

try:
	for tc in range(int(input())):
		solve()
except:
	pass


