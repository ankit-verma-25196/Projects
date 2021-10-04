# https://www.codechef.com/LTIME100C/problems/SOD3


def sum_of_digits(n):
	sum_ = 0
	for i in str(n):
		sum_+=int(i)

	return sum_


def solve():
	try:
		lr = list(map(int,input().split()))
	except:
		pass

	l = lr[0]
	r = lr[1]

	count = 0
	for i in range(l,r+1):
		if sum_of_digits(i)%3 == 0:
			count += 1
			break

#	print(i)

	mod = r%3
	r_limit = r - mod

	diff = r - i
#	print(diff)

	if diff > 0:
		count += diff//3

	print(count)

	
		


	
try:
	for tc in range(int(input())):
		solve()
except:
	pass
