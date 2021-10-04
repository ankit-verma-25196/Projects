# Given a list of size n and any one element from the List -> Pivot Element
# You need to segregate all the elements lesser than pivot on the left side and greater than pivot on the right side in any order
# Partition Algorithm
# For Quick Sort
# Pick any Random Pivot
# Partition the list based on the pivot
# Recursively apply the same above Logic - Left part and Right Part

# How to choose Pivot
# If we choose smallest element as pivot, then leads to O(n^2) Time Complexity
# Mean - can be biased as [1,10000,10001,10]
# Can't choose Median for segregation as for this - sorted list is needed
# We should have the element of randomness --> Choose Pivot Randomly
# T(n) --> no. of operations required to apply quicksort on list of size n
# Estimation(T(n)) --> calculate with using probablity -- 
# relation of random variable AND probability for calculating mean
# Sum (X.P(T(n)=X))  = value X * Prob to get X 

from random import randrange

def partition(arr, left, right):
	m = left
	pivot_index = randrange(left, right ) # we choose pivot randomly
	pivot = arr[pivot_index] # keeping track of pivot element
	arr[right], arr[pivot_index] = arr[pivot_index], arr[right] # save pivot at last index
	for i in range(left, right):
		if arr[i] <= pivot:
			arr[i], arr[m] = arr[m], arr[i]
			m += 1

	
	arr[m], arr[pivot_index] = arr[pivot_index], arr[m]
	return m

def quicksort(arr, left, right):
	if left >= right:
		# list is sorted , just return
		return

	pivot_index = partition(arr, left, right)
	quicksort(arr, left, pivot_index-1)
	quicksort(arr, pivot_index+1, right)

	return

#li = [10 , 7, 8, 9, 1, 5]
li = [1,9,3,4,1]
n = len(li)
quicksort(li, 0, n-1)

print(li)
