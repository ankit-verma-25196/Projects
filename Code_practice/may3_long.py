# XOR Equality

def solve():
	try:
		n = int(input())
	except:
		pass

	a = 2
	b = n-1
	tmp = 1

	mod = 1000000007
	while b > 0:
		if b % 2 != 0:
			tmp = (tmp * a) % mod
#		print("tmp = "+str(tmp))
		a = (a * a) % mod
#		print("a = "+str(a))
		b = b//2
#		print("b = "+str(b))


	
	print(tmp)
	
try:
	for tc in range(int(input())):
		solve()
except:
	pass

