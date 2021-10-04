# insertion sort
# example - card
# 1 2 4 3 0 - dryrun this until sorted fully
# 1 2 5 6 7 4 ,i=5 , j=4 dryrun this

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i] # this element will inserted at it's current position
		j = i - 1 # because correct position of insertion will be on left
		while j >= 0 and key < arr[j]:
			arr[j+1]=arr[j] # Here we are doing only 1 operation instead of 3 usual operations in swapping
			j -= 1

		arr[j+1] = key

li = [0,4,-1,5,4,2]

insertion_sort(li)

print(li)

# check this type of 1 operation swapping in bubble sort also - hacky swap operation

# Analysis for Insertion Sort
# TC - O(n^2)
# No . of swaps = O(n^2)
# SC = O(1)
# in place - yes
# no.of comparison = O(n^2)
# Stable -  - yes  5 4 3 2 1 1 , 5 1 1
# best case - big omega(n)

# 1 2 3 4 0 - almost sorted list(when only 1 element is not at it's right position)

