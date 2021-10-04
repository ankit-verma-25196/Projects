# https://www.codechef.com/UADS1001/problems/SIPM

def solve():
	try:
		n = int(input())
		l1 = list(map(int, input().split()))
	except:
		pass


	dic1 = {}
	for i in l1:
		if i in dic1.keys():
			dic1[i] += 1
		else:
			dic1[i] = 1


	neg = 0
	pos = 0

	for i in dic1.keys():
		if i<0:
			neg += i
		else:
			pos += i

	print(str(pos)+" "+str(neg))
			

try:
	for tc in range(int(input())):
		solve()
except:
	pass
