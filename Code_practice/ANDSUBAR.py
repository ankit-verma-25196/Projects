# https://www.codechef.com/OCT21C/problems/ANDSUBAR
import math

def solve():
	try:
		n = int(input())
	except:
		pass

	count_2 = 0
	temp = n

	while temp!=1:
		temp = temp//2
		count_2 += 1
		
#	print("count_2=",count_2)

	first_lower = int(math.pow(2,count_2))
#	print("first_lower=",first_lower)

	diff1 = (n - first_lower)+1
#	print("diff1=",diff1)

	second_lower = int(math.pow(2,count_2-1))
#	print("second_lower=",second_lower)

	diff2 = first_lower - second_lower
#	print("diff2=",diff2)

	if diff1>diff2:
		print(diff1)
	else:
		print(diff2)

try:
	for tc in range(int(input())):
		solve()
except:
	pass
