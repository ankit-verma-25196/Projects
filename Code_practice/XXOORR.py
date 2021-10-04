#https://www.codechef.com/JULY21C/problems/XXOORR

def solve():
	try:
		nk = list(map(int,input().split()))
		l1 = list(map(int,input().split()))
	except:
		pass

	n = nk[0]
	k = nk[1]

	h1 = {}
	for num in l1:
		bin_num = bin(num)	
		print(bin_num)

		s_bin_num = bin_num.lstrip('0b')

		print(s_bin_num)

		for i in range(len(s_bin_num)):
			if s_bin_num[i] == "1":
				if i in h1:
					h1[i] += 1
				else:
					h1[i] = 1

		print(h1)
		


try:
	for tc in range(int(input())):
		solve()
except:
	pass

