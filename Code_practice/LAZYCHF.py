# https://www.codechef.com/START4C/problems/LAZYCHF

def solve():
	try:
		xmd = list(map(int, input().split()))
	except:
		pass

	x = xmd[0]
	m = xmd[1]
	d = xmd[2]


	timeTaken = x*m
	upperBound = x+d
	
	print(min(timeTaken,upperBound))
try:
	for tc in range(int(input())):
		solve()
except:
	pass
