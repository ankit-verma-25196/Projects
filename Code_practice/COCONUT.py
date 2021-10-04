# https://www.codechef.com/JUNE21C/problems/COCONUT

def solve():
	try:
		xaxbXAXB = list(map(int,input().split()))
	except:
		pass

	xa = xaxbXAXB[0]
	xb = xaxbXAXB[1]
	XA = xaxbXAXB[2]
	XB = xaxbXAXB[3]

	s = (XA//xa)+(XB//xb)
	print(s)

try:
	for tc in range(int(input())):
		solve()
except:
	pass
