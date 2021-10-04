# Selection Sort

'''
1. We will have unsorted and sorted parts in the array 
2. Gradually the sorted part will increase 
3. We find minimum from the unsorted region and place it as next element in the sorted region

Analysis of the Algorithm: 

 Time Coplexity(T.C): O(n^2) 
 	n iterations(to find min from n elements) + (n-1) iterations(to find min from n-1 elements) + ... +1
	n^2 + n//2 --> Since Biggest order term here is n^2, So T.C = O(n^2)
 All - Best, Avg,Worst Case Complexities -> n^2

 Space Complexity: O(1) - We have not used any other data structure
 In-place: YES - We have use original list only for our computation
 Stable: No - as relative ordering chnages for the same elements
 No. of Comparisons - O(n^2)
 No. of Swaps - O(n)
'''

def find_min_from_unsorted_region(arr,start):
	min_index = start
	for i in range(start,len(arr)):
		if arr[i]<arr[min_index]:
			min_index = i

	return min_index

def selection_sort(arr):
	min_index = 0
	for i in range(len(arr)):
		min_index = find_min_from_unsorted_region(arr, i)
		# Do swapping now 
		arr[i],arr[min_index] = arr[min_index],arr[i]

	return arr


li = [int(i) for i in input().split()]
print("before selection sort:",li)
print("after selection sort:",selection_sort(li))


		



