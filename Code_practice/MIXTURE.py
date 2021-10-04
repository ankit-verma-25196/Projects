# https://www.codechef.com/OCT21C/problems/MIXTURE

def solve():
	try:
		ab = list(map(int,input().split()))
	except:
		pass

	a = ab[0]
	b = ab[1]

	if a>0 and b>0:
		print("Solution")	
	elif a>0 and b==0:
		print("Solid")
	elif a==0 and b>0:
		print("Liquid")

try:
	for tc in range(int(input())):
		solve()
except:
	pass


