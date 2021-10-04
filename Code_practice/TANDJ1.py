#https://www.codechef.com/LTIME96C/problems/TANDJ1

import math

def solve():
	try:
		abcdk = list(map(int,input().split()))
	except:
		pass

	a = abcdk[0]
	b = abcdk[1]
	c = abcdk[2]
	d = abcdk[3]
	k = abcdk[4]


	original_distance = abs(c-a) + abs(d-b)
#	print(original_distance)
	if original_distance == k:
		print("YES")
	elif  k > original_distance :
		diff = abs(original_distance - k)
#		print(diff)
		if diff%2 == 0:
			print("YES")
		else:
			print("NO")
	elif k < original_distance:
		print("NO")
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
