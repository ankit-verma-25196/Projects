# https://www.codechef.com/LTIME96C/problems/TWINGFT

def solve():
	try:
		nk = list(map(int,input().split()))
		l1 = list(map(int,input().split()))
	except:
		pass

	n = nk[0]
	k = nk[1]

#	print(n,k)
	l1.sort(reverse=True)
#	print(l1)

	i = 0
	turns_1 = 0
	turns_2 = 0
	s1 = 0
	s2 = 0
	while i < n:
		if turns_1 == k:
			break
		
		if turns_1 <= k:
			s1 += l1[i]
			turns_1 += 1


		if turns_2 < k:
			if turns_2 == k-1:
				s2 += l1[i+1]
				s2 += l1[i+2]
			else:
				s2 += l1[i+1]

			turns_2 += 1
	
		i += 2
		'''
		print("s1="+str(s1))
		print("s2="+str(s2))
		print()
		print("turns 1="+str(turns_1))
		print("turns 2="+str(turns_2))
		print()
		print("i="+str(i))
		'''

	if s1 > s2:
		print(s1)
	else:
		print(s2)

try:
	for tc in range(int(input())):
		solve()
except:
	pass
