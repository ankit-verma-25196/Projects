import sys
import math

def solve():
	try:
		s = input()
	except:
		pass

	if "party" not in s:
		print(s)
	else:
		print(s.replace("party","pawri"))

try:
	for tc in range(int(input())):
		solve()
except:
	pass
