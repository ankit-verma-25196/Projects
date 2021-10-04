# String Algorithms
# https://www.codechef.com/UASTR01/problems/CORUS

def solve():
	try:
		nq = list(map(int,input().split()))
		s = input()
	except:
		pass

	n = nq[0]
	q = nq[1]

	h1 = {}

	for i in s:
		if i in h1:
			h1[i]+=1
		else:
			h1[i]=1

#	print(h1)


	l1 = list(h1.values())
#	print(l1)
	
	
	try:
		for i in range(q):
			cntrs = int(input())
			
			if cntrs == 0:
				print(n)
			else:
				ans = 0
				for i in range(len(l1)):
					if l1[i]-cntrs >= 1:
						ans+= l1[i]-cntrs

				print(ans)
			
	except:
		pass

		
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
