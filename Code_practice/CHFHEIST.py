# https://www.codechef.com/JUNE21C/problems/CHFHEIST


def solve():
	try:
		DdPQ = list(map(int,input().split()))
	except:
		pass

	D = DdPQ[0]
	d = DdPQ[1]
	P = DdPQ[2]
	Q = DdPQ[3]

	s1 = 0

	div = D//d

	# initial collection
	s1 += d*P
#	print("initial s1="+str(s1))

	# collection from 1Q to (n-1)Q
	if div > 1:
		s2 = d*(P*(div-1) + ((div-1)*(div)*Q)//2)
#		print("s2 1Q to (n-1)Q="+str(s2))
		s1 += s2
		

	if D%d == 0:
		print(s1)
	else:
		rem = D%d
		s3 = (P+(div*Q))*rem
#		print("last s3="+str(s3))
		s1 += s3
		print(s1)


try:
	for tc in range(int(input())):
		solve()
except:
	pass
