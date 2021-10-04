# https://www.codechef.com/LTIME100C/problems/VDATES

def solve():
	try:
		dlr = list(map(int,input().split()))
	except:
		pass

	d = dlr[0]
	l = dlr[1]
	r = dlr[2]

	if d<l:
		print("Too Early")
	elif d>=l and d<=r:
		print("Take second dose now")
	else:
		print("Too Late")


	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
