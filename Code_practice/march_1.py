import sys
import math

def solve():
	nhx = []
	t_arr = []
	try:
		nhx = list(map(int, input().split()))
		t_arr = list(map(int, input().split()))
	except:
		pass

	n = nhx[0]
	h = nhx[1]
	x = nhx[2]

	max_t = max(t_arr)



	if max_t+x >= h:
		print("YES")
	else:
		print("NO")

try:
	solve()
except:
	pass


