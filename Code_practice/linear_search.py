def linear_search(arr, target):
	for i in range(0, len(arr)):
		if arr[i] == target:
			return i

	return -1

n = int(input()) # no need of n as we are taking list in single line

li = [int(x) for x in input().split()] # take input of integer list in single line

target = int(input())

print(linear_search(li, target))










