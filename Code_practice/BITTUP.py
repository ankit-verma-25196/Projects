# https://www.codechef.com/JUNE21C/problems/BITTUP

# using recursion
'''
def power(x,y):
	temp = 0
	if y == 0:
		return 1
	temp = power(x,int(y/2))
	if y%2 == 0:
		return temp * temp
	else:
		return x * temp * temp
'''
# using bitmasking
def power(a,b):
	res = 1
	mod = 1000000007
	while b>0:
		if b&1:
			res = (res*a)%mod

		a = (a*a)%mod
		b = b>>1

	return res
		
def solve():
	try:
		nm = list(map(int,input().split()))
	except:
		pass


	n = nm[0]
	m = nm[1]

#	div = 1000000007

#	x = (power(2,n)-1)%div
#	print(x)
#	ans = (power(x,m))%div

	ans = power(power(2,n)-1,m)

	print(ans)
try:
	for tc in range(int(input())):
		solve()
except:
	pass
