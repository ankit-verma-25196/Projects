# Solubility

def solve():
	try:
		xab = list(map(int,input().split()))
	except:
		pass

	x = xab[0]
	a = xab[1]
	b = xab[2]

	first = (100-x)*b
	second = a + first
	final= second*10

	print(final)

try:
	for tc in range(int(input())):
		solve()
except:
	pass

