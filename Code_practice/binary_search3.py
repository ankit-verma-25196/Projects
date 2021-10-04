# binary search 3
# Ques - Given sorted list and integer X.Find the first value in the list which is greater than or equal to X.

def binary_search(arr, target):
	# first of all we will define the search space
	n = len(arr)
	left, right = 0, n-1 # boundaries of the search space
	while left<= right:
		mid = (left+right) // 2
		if arr[mid] >= target:
			return mid
		elif arr[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	
	return -1

li = [0, 5, 10, 19, 33, 45, 56, 68]
pos = binary_search(li, 11)
print(li[pos-1])

# TC - O(log n), Omega(1), Theta(1)
