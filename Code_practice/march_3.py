# march 3 - interesting XOR

import math
import sys

def solve():
	try:
		c = int(input())
	except:
		pass

	if c == 1:
		print("0")
	elif c == 2:
		print("0")
	else:
		d = 0
		while 2**d < c:
			d += 1

	#	print(d)

		li = []
		for i in range(2**d):
			for j in range(i+1,2**d):		
				if i^j == c:
					li.append(i*j)	

		print(li)
		print(max(li))

try:
	for tc in range(int(input())):
		solve()
except:
	pass


