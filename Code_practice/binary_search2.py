# recursive binary search
# S.C = O(log n)

# python has large limits of integer - let's say if limit is same as in c++ --> 2147483647  to -2147483648

# l+r value can increase the integer bucket in some languages
# to prevent the issue of overflow we can get mid value as:
# mid = L +(R-L)/2 --> modified mid
# (L+R+L-L)/2 --> 2L/2+(R-L)/2 --> L +(R-L)/2

# So we have Sorted Rotated List - [3,6,8,10,15,0,1,2], target--> 1
# TC --> O(log n), SC -->O(1)
# In 1 Second , number of iterations -- 10^8
# Assignments present in discord

def binary_search(arr, target):
	n = len(arr)
	start, end = 0, n-1

	while start <= end:
		mid = start + (end- start)//2
		if arr[mid] == target:
			return mid
		elif arr[mid] >= arr[start]:
			#case 1
			if target >= arr[start] and target < arr[mid]:
				end = mid - 1
			else:
				start = mid + 1
		else:
			#case 2
			if target <= arr[end] and target > arr[mid]:
				start = mid + 1
			else:
				end = mid - 1

	return -1

li = [int(x) for x in input().split()] #take input of ineger list
target = int(input())
print(binary_search(li, target))

