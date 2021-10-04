# Gold Collection - https://www.codechef.com/problems/GOLDTRIP

def solve():
	try:
		n = int(input())
		l1 = list(map(int,input().split()))
	except:
		pass

	#making prefix sum array

	prefix = [0]*(n)
	prefix[0]=l1[0]

	
	for i in range(1,n):
		prefix[i] = l1[i]+prefix[i-1]

#	print(prefix)

	try:
		q = int(input())
	except:
		pass

	while q>0:
		try:
			l,r=[int(x) for x in input().split()]
#			print(l)
#			print(r)
		except:
			pass

		s = (prefix[r-1]-prefix[l-1])+l1[l-1]
		print(s)
		q-=1
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
