

def solve():
	try:
		Mxy = list(map(int, input().split()))
		l1 = list(map(int, input().split()))
	except:
		pass

	M = Mxy[0]
	x = Mxy[1]
	y = Mxy[2]

	dist = x*y

	min = l1[0]-dist
	if min < 0:
		min = 1
	max = l1[0]+dist

	l = len(l1)
	for i in range(1..l):
		print(i)
	
		

	

try:
	for tc in range(int(input()))
		solve()
except:
	pass

