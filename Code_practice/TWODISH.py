# https://www.codechef.com/LTIME100C/problems/TWODISH

'''
2 2 2 = 2
3 2 3 = 2
1 2 3 = 2
3 2 1 = 2

3 4 1 = 4
'''


def solve():
	try:
		nabc = list(map(int,input().split()))
	except:
		pass

	n = nabc[0]
	a = nabc[1]
	b = nabc[2]
	c = nabc[3]

	sum_ac = a+c
	min_ac_b = min(sum_ac,b)


	if min_ac_b >= n:
		print("YES")
	else:
		print("NO")

		
try:
	for tc in range(int(input())):
		solve()
except:
	pass
