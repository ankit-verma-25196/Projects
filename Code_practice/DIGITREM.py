# https://www.codechef.com/OCT21C/problems/DIGITREM

def solve():
	try:
		nd = list(map(int,input().split()))
	except:
		pass

	n = nd[0]
	d = nd[1]

	if str(d) not in str(n):
		print("0")
	else:
		digits_n = 0
		indexes_d = []
		for i in range(len(str(n))):
			if str(n)[i] == str(d):
				indexes_d.append(i)
			digits_n += 1

		print("digits_n=",digits_n)
		print("indexes_d=",indexes_d)
				

	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
