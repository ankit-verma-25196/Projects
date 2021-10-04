# https://www.codechef.com/SEPT21C/problems/TRAVELPS

def solve():
	try:
		nab = list(map(int,input().split()))
		s = input()
	except:
		pass

	
	a = nab[1]
	b = nab[2]

	zeroes_cnt = 0
	ones_cnt = 0

	for i in s:
		if i == '0':
			zeroes_cnt += 1
		else:
			ones_cnt += 1

	total = (a*zeroes_cnt)+(b*ones_cnt)

	print(total)

try:
	for tc in range(int(input())):
		solve()
except:
	pass
