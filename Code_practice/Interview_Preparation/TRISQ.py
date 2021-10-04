# https://www.codechef.com/INPREP01/problems/TRISQ

def solve():
	try:
		n = int(input())
	except:
		pass

#	print(n)

	if n == 1 or n == 2 or n == 3:
		print("0")
	else:
		steps = 0
		if n % 2 == 0:
			steps = n - 4
		else:
			steps = n - 5

		steps = steps // 2

#		print(steps)
		num = 1
		for i in range(steps):
			num += i+2

		print(num)

try:
	for tc in range(int(input())):
		solve()
except:
	pass

