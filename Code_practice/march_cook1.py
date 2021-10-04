import sys
import math

def solve():
	try:
		w1w2x1x2m = list(map(int,input().split()))
	except:
		pass

	w1 = w1w2x1x2m[0]
	w2 = w1w2x1x2m[1]
	x1 = w1w2x1x2m[2]
	x2 = w1w2x1x2m[3]
	m = w1w2x1x2m[4]

	diff = w2-w1

	low = x1*m
	high = x2*m

	if diff < low or diff > high:
		print("0")
	else:
		print("1")

try:
	for tc in range(int(input())):
		solve()
except:
	pass
