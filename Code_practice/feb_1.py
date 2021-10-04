import sys
import math

def solve():
	try:
		nk=list(map(int,input().split()))
	except:
		pass

	n=nk[0]
	k=nk[1]

	if n < k:
		print(str(n))

	elif n == k:
		print("0")

	elif n > k:
		ans = 0
		while n >= k:
			n = n-k
			
		print(n)
			
try:
	for tc in range(int(input())):
		solve()
except:
	pass

