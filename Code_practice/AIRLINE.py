# https://www.codechef.com/SEPT21C/problems/AIRLINE

def solve():
	try:
		abcde = list(map(int,input().split()))
	except:
		pass

#	print(abcde)
	a = abcde[0]
	b = abcde[1]
	c = abcde[2]
	d = abcde[3]
	e = abcde[4]

	ab = a+b
	bc = b+c
	ac = a+c

	if (ab<=d and c<=e) or (bc<=d and a<=e) or (ac<=d and b<=e):
		print("YES")
	else:
		print("NO")


try:
	for tc in range(int(input())):
		solve()
except:
	pass
