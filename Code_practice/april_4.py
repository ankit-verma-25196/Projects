import sys
import math

def solve():
	try:
		n = int(input())
	except:
		pass

	total_sum = 21
	sum_n1 = 0
	sum_n2 = 0
	sum_n3 = 0
	sum_n4 = 0

	level = int(n/4)
	rem = n%4

#	print(level)
#	print(rem)

	#pre calculated Ist level sums:
	sum_n1 = total_sum - 1
	sum_n2 = (2*total_sum) - 2*(1+2)
	sum_n3 = (3*total_sum) - (3*(1+2) + 3)
	sum_n4 = (4*total_sum) - 4*(1+2+3)
	sum_n5 = 3*(4+5+6) + 1*(5+6) + 20
	sum_n6 = 2*(4+5+6) + 2*(5+6) + 36
	sum_n7 = 1*(4+5+6) + 3*(5+6) + 51
	sum_n8 = 4*(5+6) + 60


	'''
	1 -> 2+3+4+5+6
	2 -> 2*(3+4+5+6) = 2*18 =36

	3 -> (4+5+6) + 2*(3+4+5+6)  = 15 + 2*18 = 15+36 = 51

	4 -> 4*(4+5+6) = 4*15 = 60

	5 -> 3*(4+5+6) + 1*(5+6) + 20 = 45 +11 + 20 = 45+31 = 76
	
	6 -> 2*(4+5+6) + 2*(5+6) + 36 = 30 + 22 + 36 = 52 + 36 = 88

	7 -> 1*(4+5+6) + 3*(5+6) + 51 = 15 + 33 + 51 = 66+33= 99

	8 -> 4*(5+6) + 60 = 44+60 = 104

	9 -> (level-1)*44 as here level = 2(9/4) + sum_n5
	10 -> 44 + sum_n6 = 44 + 88 = 132
	'''

	if n == 1:
		print(sum_n1)
	elif n == 2:
		print(sum_n2)
	elif n == 3:
		print(sum_n3)
	elif n == 4:
		print(sum_n4)
	
	elif n == 5:
		print(sum_n5)
	elif n == 6:
		print(sum_n6)
	elif n == 7:
		print(sum_n7)
	elif n == 8:
		print(sum_n8)
	else:
		level = int(n/4)
		rem = n%4
		
		sum_new = 0
		if rem == 1:
			sum_new = (level-1)*44 + sum_n5 
		elif rem == 2:
			sum_new = (level-1)*44 + sum_n6
		elif rem == 3:
			sum_new = (level-1)*44 + sum_n7
		elif rem == 0:
			sum_new = (level-2)*44 + sum_n8

		print(sum_new)


	'''
	if level == 0:
		if n == 1:
			print(sum_n1)
		elif n == 2:
			print(sum_n2)
		elif n == 3:
			print(sum_n3)
		elif n == 4:
			print(sum_n4)

	elif level == 1 and rem > 0:
		new_sum = sum_n4 +
	elif level > 0 and rem == 0:
		sum_rem0 = level*(sum_n4) - (level-1)*24
		print(sum_rem0)

	elif level > 0 and rem > 0:
		initial_sum = level*(sum_n4) - (level-1)*24 - rem*6
#		print(initial_sum)
		sum_remgt0 = 0
		if rem == 1:
			sum_remgt0 = initial_sum + sum_n1
		elif rem == 2:
			sum_remgt0 = initial_sum + sum_n2
		elif rem == 3:
			sum_remgt0 = initial_sum + sum_n3
		elif rem == 4:
			sum_remgt0 = initial_sum + sum_n4

		print(sum_remgt0)
		'''

try:
	for tc in range(int(input())):
		solve()
except:
	pass
