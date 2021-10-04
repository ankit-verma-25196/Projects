# march 3 - interesting XOR

import math
import sys

def solve():
	try:
		c = int(input())
	except:
		pass

	d = 0
#	print(pow(2,3))
			
	
	while 2**d <= c:
		d += 1

#	print(d)
	'''
	li = []
	li2 = []
	for i in range(2**d):
		for j in range(i+1,2**d):		
			if i^j == c:
				li2.append("i="+str(i)+"j="+str(j))
				li.append(i*j)	
	'''

	low = 2**(d-1)
	high = 2**d
#	print(str(low)+" "+str(high))
	li3=[]

	diff = c - (low-1)
	k = high - diff

	ans = (low-1) * k
	print(ans)

	'''
	for k in range(low,high):
		if (low-1)^k == c:
			li3.append((low-1)*k)

	print(li3[0])
	'''

#	print(li2)
#	print(li)

#	print(max(li3))

try:
	for tc in range(int(input())):
		solve()
except:
	pass


