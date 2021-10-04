# https://www.codechef.com/SDPCB21/problems/KTTABLE

def solve():
	try:
		n = int(input())
		a = list(map(int,input().split()))
		b = list(map(int,input().split()))
	except:
		pass

	count = 0
	for i in range(n):
		diff = 0
		if i == 0:
			diff = a[i]
		else:
			diff = a[i]-a[i-1]


		if diff>=b[i]:
			count += 1

	print(count)
			
			

	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
