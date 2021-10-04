# Bubble sort
'''
Which bubble will come up first - bigger bubble / small bubble
bigger bubble because --> Terminal Velocity =~ Radius^2
Stokes Law - main intuition behind Bubble Sort

Comparisons - n+(n-1)+..... ->Time Complexity O(n^2)
Space Complexity - only 1 list O(1)
Swaps - O(n^2)
Stability (Relative Ordering of elements) --> Stable

Best Case - omega(n)
'''

def bubble_sort(arr):

	for i in range(0,len(arr)):
		swapped = False # ensures
		for j in range(0,len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j] # Do Swapping
				swapped = True
		
		if not swapped:
			return

	return 


li = [5,4,3,2,1]		

bubble_sort(li)

print(li)

