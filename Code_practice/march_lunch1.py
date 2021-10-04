import sys
import math

def solve():
	try:
		nx = list(map(int, input().split()))
	except:
		pass

	n = nx[0]
	x = nx[1]
	
#	print(n)
#	print(x)


	r_arr = []
	while n > 0:
		try:
			sr = list(map(int, input().split()))
		except:
			pass

		s = sr[0]
		r = sr[1]

#		print(s)
#		print(r)

		
		if s <= x:
			r_arr.append(r)
			

		n -= 1

	print(max(r_arr))

try:
	for tc in range(int(input())):
		solve()
except:
	pass


