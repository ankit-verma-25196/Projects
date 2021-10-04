# bisect in python
import bisect

arr = [int(x) for x in input().split()]

while True:
	ch = input()
	if ch == 'l':
		x = int(input())
		print(bisect.bisect_left(arr,x)) # O(log n)
	elif ch == 'r':
		x = int(input())
		print(bisect.bisect_right(arr,x)) # O(log n)
	else:
		break
