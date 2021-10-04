#!/usr/bin/python3

# bubble sort



def bubble_sort(arr):
	

	for i in range(0,len(arr)):
		swapped = False
		for j in range(0,len(arr)-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j] # Do Swapping
				swapped = True

		if not swapped:
			return
			
		import pdb;pdb.set_trace()

	return

li = [5,4,3,2,1]

bubble_sort(li)

print(li)


