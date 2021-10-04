# inversion count

def merge(arr, left, mid, right):
	temp = [0]*(right - left + 1)
	i, j, k = left, mid+1 , 0
	while i <= mid and j <= right:
		
	

def mergesort(arr, left, right):
	if left < right :
		mid = (left + right) // 2
		count_left = mergesort(arr, left, right)
		count_right = mergesort(arr, left, right)
		count_mergers = merge()
		return count_left + count_right + count_mergers

	return 0


