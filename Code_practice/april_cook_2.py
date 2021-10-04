# April cook 2
from collections import Counter

def solve():
	try:
		nx = list(map(int,input().split()))	
		arr = list(map(int,input().split()))

	except:
		pass

	x = nx[1]

	arr_set = list(set(arr))
	
	print(arr_set)

	arr_hash = Counter(arr)
	print(dict(arr_hash))
try:
	for tc in range(int(input())):
		solve()
except:
	pass
