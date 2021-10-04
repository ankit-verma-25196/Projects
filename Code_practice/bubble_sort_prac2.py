# Bubble sort

'''
> Comparison Based Sorting
> As per Stokes Law: Terminal velocity is directly proportional to Radius^2
> After each iteration, biggest element of unsorted region moves to the last correct position

Time Complexity: Worst case : O(n^2)
Space Complexity: O(1)
In-place: YES
No. of comparisons: O()
No. of Swaps: O()

'''

def bubble_sort(arr):
	for i in range(len(arr)-1):
		swapped = False
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				# Do Swapping
				arr[j],arr[j+1] = arr[j+1],arr[j]
				swapped = True
		print(arr)

		if not swapped:
			return arr

	return arr

li = [int(i) for i in input().split()]
print("before bubble sort:",li)
print("after bubble sort:",bubble_sort(li))
