import sys
import math

def solve():
	try:
		s = input()
	except:
		pass

#	print(s)

	count_one = 0
	gp = 0
	for i in range(len(s)):
#		print(s[i])
		if s[i] == '1':
			count_one += 1
		else:
			if count_one > 0:
				gp += 1
			count_one = 0

	if count_one > 0:
		gp += 1
	
	print(gp)



try:
	for tc in range(int(input())):
		solve()
except:
	pass

