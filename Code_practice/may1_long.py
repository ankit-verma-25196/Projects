# Golf
def solve():
	try:
		nxk = list(map(int,input().split()))
	except:
		pass

	n = nxk[0]
	x = nxk[1]
	k = nxk[2]

#	if n%2 != 0: # when n is odd
#	else: # when n is even

	if x % k == 0: # Checking from start
		print("YES")
	else:
		diff = (n+1) - x
		if diff % k == 0:
			print("YES")
		else:
			print("NO")
		
try:
	for tc in range(int(input())):
		solve()
except:
	pass

