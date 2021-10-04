# Ques - Given an unsorted list , find any element a[i] such that a[i]>a[i-1] and a[i]>a[i+1]
# There can be multiple a[i], find any one of them. Return the index.

# [1,2,3,1] --> ans is element= 3 , index =2

'''
Another approach without corner case
def find_peak(arr):
	lo,hi = 0, len(arr)-1
	while lo < hi:
		mid = lo + (hi-lo)//2
		
		if arr[mid] > arr[mid+1]:
			#case 2
			hi = mid
		else:
			lo = mid + 1

	return lo
'''

def find_peak(arr):
	lo,hi = 0, len(arr)-1
	while lo <= hi:
		mid = lo + (hi-lo)//2
		#corner case
		if mid+1 < len(arr) and mid-1 >= 0 and arr[mid] > arr[mid+1] and arr[mid] >arr[mid-1]:
			return mid
		
		if arr[mid] > arr[mid+1]:
			#case 2
			hi = mid - 1
		else:
			lo = mid + 1

	return lo


	
	
