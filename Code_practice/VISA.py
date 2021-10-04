# https://www.codechef.com/COOK130C/problems/VISA

def solve():
	try:
		x1x2y1y2z1z2 = list(map(int,input().split()))
	except:
		pass

	x1 = x1x2y1y2z1z2[0]
	x2 = x1x2y1y2z1z2[1]
	y1 = x1x2y1y2z1z2[2]
	y2 = x1x2y1y2z1z2[3]
	z1 = x1x2y1y2z1z2[4]
	z2 = x1x2y1y2z1z2[5]

	if x2>=x1 and y2>=y1 and z2<=z1:
		print("YES")
	else:
		print("NO")
try:
	for tc in range(int(input())):
		solve()
except:
	pass
