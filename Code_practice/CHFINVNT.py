# https://www.codechef.com/AUG21C/problems/CHFINVNT


def solve():
	try:
		npk = list(map(int, input().split()))
	except:
		pass

	n = npk[0]
	p = npk[1]
	k = npk[2]

	print(n,p,k)


	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
