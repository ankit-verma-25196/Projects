# https://www.codechef.com/OCT21C/problems/THREEBOX

def solve():
	try:
		abcd = list(map(int,input().split()))
	except:
		pass


	a = abcd[0]
	b = abcd[1]
	c = abcd[2]
	d = abcd[3]

	abc = a + b + c
	ab = a + b
	ac = a + c
	bc = b + c

	if abc <= d:
		print("1")
	elif ab <= d or ac <= d or bc <= d:
		print("2")
	else:
		print("3")

	
try:
	for tc in range(int(input())):
		solve()
except:
	pass


