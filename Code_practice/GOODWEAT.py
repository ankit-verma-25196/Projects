# https://www.codechef.com/START12C/problems/GOODWEAT

def solve():
	try:
		l1 = list(map(int,input().split()))
	except:
		pass


	flag = 0
	count1 = 0
	for i in l1:
		if i == 1:
			count1 += 1

	if count1>3:
		print("YES")
	else:
		print("NO")
try:
	for tc in range(int(input())):
		solve()
except:
	pass
