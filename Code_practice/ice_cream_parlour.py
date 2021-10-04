#ice cream parlour

def binary_search(arr, left, target):
	n = len(arr)
	right = n-1
	while left <= right:
		mid = (left+right) // 2
		if arr[mid] == target:
			return arr[mid]
		elif arr[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	
	return -1
	

def solve():
	try:
		money = int(input())
		n = int(input())
		li = list(map(int, input().split()))	
	except:
		pass

#	print(li)
#	print(money)

	dict1 = {}
	for i in range(len(li)):
		dict1[i+1]=li[i]

#	print(dict1)

	arr = sorted(li)
#	print(arr)

	other = -1
	pos_other = 0
	for i in range(len(li)):
		diff = money - arr[i]
#		print("diff = "+str(diff))
		other = binary_search(arr, i, diff)
		if other != -1:
			break

#	print(arr[i])
#	print(other)

	val_list = list(dict1.values())
	position1 = val_list.index(arr[i])
#	print(position1+1)
	
	if arr[i] == other:
		position2 = position1 + 1
	else:
		position2 = val_list.index(other)
	if position1 < position2:
		print(str(position1+1)+" "+str(position2+1))
	else:
		print(str(position2+1)+" "+str(position1+1))

	
		
		
		
		
try:
	for tc in range(int(input())):
		solve()
except:
	pass
