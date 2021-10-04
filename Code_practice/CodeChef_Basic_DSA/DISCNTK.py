# https://www.codechef.com/UADS1001/problems/DISCNTK

def solve():
	try:
		nk = list(map(int,input().split()))
		l1 = list(map(int,input().split()))
	except:
		pass

	n = nk[0]
	k = nk[1]

	l = 0
	r = k-1

#	print(l1)
	while r != n:
		l2 = l1[l:r+1]
#		print(l2,end=" ")

		print(len(set(l2)),end=" ")
		l += 1
		r += 1

	print()
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
