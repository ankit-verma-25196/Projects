import sys
import math

def solve():
	try:
		nk = list(map(int,input().split()))
		s = input()
	except:
		pass

	n = nk[0]
	k = nk[1]

	
	count = 0
	r = 0
	'''
	while r<n:
		if count == k:
			break
		if s[r] == "*":
			r += 1
			count += 1
		else:
			if r == n-2:
				r += 1
			else:
				r += 2
	'''
	while r<n:
		if count == k:
			break
		if s[r] == "*":
			count += 1
		else :
			count = 0
		r += 1

#	print(r)
#	print(count)
	if count == k:
		print("YES")
	else:
		print("NO")

		
try:
	for tc in range(int(input())):
		solve()
except:
	pass


